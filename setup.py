#!/usr/bin/env python

from distutils.core import setup

setup(name='oxford_term_dates',
      version='1.3.0',
      description='A Python library for translating between real dates and Oxford term dates',
      author='IT Services, University of Oxford',
      author_email='mobileoxford@it.ox.ac.uk',
      url='https://github.com/ox-it/oxford-term-dates',
      packages=['oxford_term_dates','oxford_term_dates.templatetags'],
      classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Internet',
      ],
     )
