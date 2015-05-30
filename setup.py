from setuptools import setup
import sys

setup(name='image_resizer',
      version='0.0.1',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Sriram Sundarraj',
      author_email='sriram.s.1994@gmail.com',
      packages=['image_resizer'],
      entry_points={
          'console_scripts': ['image-resize=image_resize:console_main'],
      },
      url='https://github.com/srirams6/image_resizer/',
      description='Python tool to resize a bunch of images quickly.',
      classifiers=[
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities'
      ],
      )
