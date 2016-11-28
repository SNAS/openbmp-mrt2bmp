#!/usr/bin/env python

from distutils.core import setup

setup(name='openbmp-mrt',
      version='0.1.0',
      description='OpenBMP MRT',
      author='Tim Evens',
      author_email='tim@openbmp.org',
      url='',
      data_files=[('etc', ['src/etc/openbmp-mrt2bmp.yml'])],
      package_dir={'openbmp': 'src/site-packages/openbmp', 'openbmp.mrt2bmp': 'src/site-packages/openbmp/mrt2bmp'},
      packages=['openbmp', 'openbmp.mrt2bmp'],
      install_requires=['pyyaml',],
      scripts=['src/bin/openbmp-mrt2bmp']
     )

