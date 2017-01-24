#!/usr/bin/env python
import os
import sys

#from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

# setup(
# ext_modules = cythonize("sciquence/sequences/cy_searching.pyx", include_path = [np.get_include()])
# )


## TODO: debug setuptools & cython

try:
    from setuptools import setup, find_packages, Extension, Command
except ImportError:
    from distutils.core import setup,  Extension, Command


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# with open('sciquence/__init__.py') as fid:
#     for line in fid:
#         if line.startswith('__version__'):
#             VERSION = line.strip().split()[-1][1:-1]
#             break



# Install requires

with open('requirements.txt') as fid:
    INSTALL_REQUIRES = [l.strip() for l in fid.readlines() if l]

readme = open('README.rst').read()


# Doclink
doclink = """
Documentation
-------------
The full documentation is at http://sciquence.rtfd.org."""
#history = open('HISTORY.rst').read().replace('.. :changelog:', '')


# Version
VERSION = '0.1.1'


# Cython

extensions = [
    # Extension("sciquence.utils.cy_mat_utils", ["sciquence/utils/cy_mat_utils.pyx"],
    #           include_dirs=[np.get_include()]),
    Extension("sciquence.sequences.cy_searching", ["sciquence/sequences/cy_searching.pyx"],
              include_dirs=[np.get_include()]),
    Extension("sciquence.dtw.cy_segmental_dtw", ["sciquence/dtw/cy_segmental_dtw.pyx", "sciquence/dtw/cy_utils.pyx"],
              include_dirs=[np.get_include()]),

    ]

extensions =  cythonize(extensions)
#extensions =  cythonize("sciquence/sequences/cy_searching.pyx", include_path = [np.get_include()])

#print extensions


# Classifiers

classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
    ]


setup(
    name='sciquence',
    version=VERSION,
    description='Time series & sequence processing in Python',
    long_description=readme + '\n\n' + doclink + '\n\n',  #+ history,
    author='Krzysztof Joachimiak',
    # author_email='',
    url='https://github.com/krzjoa/sciquence',
    packages=find_packages(where='.', exclude=('tests')),
    package_dir={'sciquence': 'sciquence'},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    license='MIT',
    zip_safe=False,
    ext_modules=extensions,
    keywords='sciquence',
    classifiers=classifiers,
)