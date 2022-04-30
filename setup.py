from setuptools import setup, find_packages

from . import __version__

with open('README.md') as readme:
    readme_content = readme.read()

setup(name='libdbooks',
      version=__version__,
      url='https://github.com/manugram/libdbooks',
      license='GNU General Public License v3 (GPLv3)',
      author='Manuel Soto',
      author_email='manugram.dev@gmail.com',
      description='A library that provides a Python 3 interface for www.dbooks.org API.',
      keywords="dbooks",
      packages=find_packages(exclude=['test',
                                      'libdbooks.cuda-proj',
                                      '.cudatext',]),
      long_description=readme_content,
      long_description_content_type="text/markdown",
      zip_safe=False,
      )