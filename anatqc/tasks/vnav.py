import os
import re
import glob
import json
import shutil
import logging
import tempfile as tf
import anatqc.tasks as tasks
from anatqc.state import State
from executors.models import Job
from anatqc.bids import BIDS

logger = logging.getLogger(__name__)

class Task(tasks.BaseTask):
    def __init__(self, infile, outdir, tr, tempdir=None, pipenv=None):
        self._infile = infile
        self._tr = tr
        self.job = None
        super().__init__(outdir, tempdir, pipenv)

    def build(self):
        cmd = [
            'selfie',
            '--lock',
            '--output-file', self._prov,
            'parse_vNav_Motion.py',
            '--input-dir', self._infile,
            '--tr', str(self._tr),
            '--rms',
            '--max',
            '--plot',
            '--output-dir', self._outdir
        ]
        if self._pipenv:
            os.chdir(self._pipenv)
            cmd[:0] = ['pipenv', 'run']
        # copy json sidecar into output logs directory
        image = self._infile.replace('sourcedata', '')
        sidecar = BIDS.sidecar_for_image(image)
        # split numbering varies by scanner (split-1.. on E11, split-8001.. on XA60),
        # so use the lowest-numbered split sidecar and store it as split-1 for Report
        pattern = sidecar.replace('_T1vnav', '_split-*_T1vnav')
        candidates = sorted(glob.glob(pattern),
                            key=lambda f: int(re.search(r'_split-(\d+)_', f).group(1)))
        if not candidates:
            logger.warning('vNav sidecar not found %s, skipping vnav', pattern)
            return
        sidecar = candidates[0]
        logdir = self.logdir()
        destination = os.path.join(logdir, os.path.basename(pattern).replace('split-*', 'split-1'))
        logger.debug('copying %s to %s', sidecar, destination)
        shutil.copy2(sidecar, destination)
        # return job object
        logfile = os.path.join(logdir, 'anatqc-vnav.log')
        self.job = Job(
            name='anatqc-vnav',
            time='10',
            memory='1G',
            command=cmd,
            output=logfile,
            error=logfile
        )

