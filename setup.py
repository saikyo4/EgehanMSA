from setuptools import setup, find_packages

setup(
    name='EgehanMSA',
    version='0.1.0',
    description='A Multiple Sequence Alignment Tool using Dynamic Programming',
    author='Egehan Alacam',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
)