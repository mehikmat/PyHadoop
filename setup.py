# meta file for project distribution
import os, sys
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now
# 1) we have a top level README.md file and 
# 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'hadoopy',
  packages = ['hadoopy'], # this must be the same as the name above
  version = '0.1',
  description = 'Python based hadoop command-line interface',
  author = 'Hikmat Dhamee',
  author_email = 'me.hemant.available@gmail.com',
  license = "MIT",
  platforms = ["any"],
  url = 'https://github.com/mehikmat/PyHadoop', # use the URL to the github repo
  download_url = 'https://github.com/mehikmat/PyHadoop/tarball/0.1', # I'll explain this in a second
  keywords = ['hadoop', 'python', 'command-line'], # arbitrary keywords
  long_description=open('README.md').read(),
  classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utilities",
        "License ::MIT License",
    ],
  entry_points={
        "console_scripts": [
            "hadoopy=hadoopy:main",
            "hadoopy%s=hadoopy:main" % sys.version[:1],
            "hadoopy%s=hadoopy:main" % sys.version[:3],
        ],
    },
)