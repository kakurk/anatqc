import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'yaxil',
    'selfie',
    'executors',
    'morphometry @ git+https://github.com/kakurk/morphometry.git@openmp#egg=morphometry', 
    'vnav'
]

test_requirements = [
]

about = dict()
with open(os.path.join(here, 'anatqc', '__version__.py'), 'r') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(),
    package_data={
        '': ['*.tar.gz', '*.yaml']
    },
    include_package_data=True,
    scripts=[
        'scripts/anatQC.py'
    ],
    install_requires=requires,
    tests_require=test_requirements
)
