from setuptools import setup
import sys

setup(name = 'image-resizer',
      description = 'Python tool to resize a bunch of images quickly.',
      long_description=open('README.rst').read(),
      version = '0.1.1',
      install_requires = [
        r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author = 'Sriram Sundarraj',
      author_email = 'ssundarraj@gmail.com',
      packages = ['image-resizer'],

      entry_points = {
          'console_scripts': ['image-resize=image_resize:console_main'],
      },
      url = 'https://github.com/ssundarraj/image-resize/',
      download_url = 'https://github.com/ssundarraj/image-resize/tarball/v0.1.0',
      keywords = ['image', 'resize', 'utility', 'compress'],
      classifiers = [
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      )
