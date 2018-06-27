#!/usr/bin/env python
import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='grid_draw',
                 version='0.0.1',
                 author='Thomas Edlich',
                 author_email='thomas.edlich@icloud.com',
                 description="An OpenAI Gym Environment to draw on a grid.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/te95/grid_draw",
                 packages=setuptools.find_packages(),
                 install_requires=['gym', 'numpy']
                 )
