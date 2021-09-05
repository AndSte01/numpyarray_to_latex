from setuptools import setup, Extension
import setuptools
import os
import sys

# get __version__, __author__, and __email__
exec(open("./numpyarray_to_latex/metadata.py").read())

setup(
    name='numpyarray_to_latex',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/benmaier/numpyarray_to_latex',
    license=__license__,
    description="A short description of the package.",
    long_description='',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
                'numpy>=1.0',
    ],
    tests_require=['pytest', 'pytest-cov'],
    setup_requires=['pytest-runner'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 ],
    project_urls={
        'Documentation': 'http://numpyarray_to_latex.benmaier.org',
        'Contributing Statement': 'https://github.com/benmaier/numpyarray_to_latex/blob/master/CONTRIBUTING.md',
        'Bug Reports': 'https://github.com/benmaier/numpyarray_to_latex/issues',
        'Source': 'https://github.com/benmaier/numpyarray_to_latex/',
        'PyPI': 'https://pypi.org/project/numpyarray_to_latex/',
    },
    include_package_data=True,
    zip_safe=False,
)
