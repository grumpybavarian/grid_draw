import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='grid_draw',
                 version='0.0.2',
                 author='Thomas Edlich',
                 author_email='thomas.edlich@icloud.com',
                 license='MIT',
                 description="An OpenAI Gym Environment to draw on a grid.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/te95/grid_draw",
                 install_requires=['gym', 'numpy']
                 )
