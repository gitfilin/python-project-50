from setuptools import setup, find_packages

setup(
    name='hexlet-code',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gendiff=gendiff.scripts.gendiff:main',
        ],
    },
)
