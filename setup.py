from distutils.core import setup
from setuptools import find_packages

setup(
    name='detr',
    description="Detection Transformers (DETR) with Python",
    version='0.0.1',
    packages=find_packages(),
    license='MIT License',
    url="https://github.com/sainavaneet/detr",
    long_description=open('README.md').read(),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8.10",
    ],
)
