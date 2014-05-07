# meta file for distribution
from distutils.core import setup
setup(
  name = 'hadoopy',
  packages = ['hadoopy'], # this must be the same as the name above
  version = '0.1',
  description = 'Python based hadoop command-line interface',
  author = 'Hikmat Dhamee',
  author_email = 'me.hemant.available@gmail.com',
  license = "http://opensource.org/licenses/MIT",
  platforms = ["any"],
  url = 'https://github.com/mehikmat/PyHadoop', # use the URL to the github repo
  download_url = 'https://github.com/mehikmat/PyHadoop/tarball/0.1', # I'll explain this in a second
  keywords = ['hadoop', 'python', 'command-line'], # arbitrary keywords
  classifiers = [],
)