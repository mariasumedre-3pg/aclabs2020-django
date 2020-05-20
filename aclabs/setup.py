#!/usr/bin/env python

import setuptools

setup(name='ACLabs Todo Project',
      version='1.0',
      description='Learn Django and GraphQL with a Todo app',
      author='ACLabs2020',
      author_email='aclabs2020@example.com',
      url='https://www.aclabs2020.com',
      packages=setuptools.find_packages(),
      include_package_data=True,
      install_requires=[
          "django==2.1.12",
          "graphene-django==2.8.2"
      ]
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Productivity :: Tools',
          ],
     )