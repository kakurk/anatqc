# Anatomical Quality Control (beta)
AnatQC is an automated quality control pipeline for T1-weighted (with or 
without volumetric navigators) MRI scans. AnatQC is built on top of the 
excellent [`dcm2niix`](https://github.com/rordenlab/dcm2niix), 
[`FreeSurfer`](https://surfer.nmr.mgh.harvard.edu/), 
[`vNav`](https://github.com/mharms/parse_vNav_Motion), 
and [`MRIQC`](https://mriqc.readthedocs.io/en/stable/) packages.

For the latest documentation please head over to [anatqc.readthedocs.io](https://anatqc.readthedocs.io).

# BU's ANATQC

This repository has a custom, modified version of the Harvard ANATQC routine. The changes to the repository include:

1. Upgrading to the latest version of Freesurfer (freesurfer/8.0.0)
2. Creating a multistage version of the Dockerfile