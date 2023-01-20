import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), "r").read()

def get_version():
    g = {}
    exec(open(os.path.join("consistency_enforcement", "Version.py"), "r").read(), g)
    return g["Version"]

setup(
    name = "consistency_enforcement",
    version = get_version(),
    author = "Igor Mandrichenko",
    author_email = "ivm@fnal.gov",
    description = ("Common modules and scripts for Rucio consistency enforcement"),
    license = "BSD 3-clause",
    url = "https://github.com/rucio/consistency-enforcement",
    packages=['consistency_enforcement'],
    long_description="Common modules and scripts for Rucio consistency enforcement", #read('README'),
    zip_safe = False
)