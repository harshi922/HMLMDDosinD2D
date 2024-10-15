# build ML app as a package thro pypi

from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOR = "-e ."
def get_requirements(filename: str) -> List[str]:
    '''Read requirements file and return list of requirements'''
    requirements = []
    with open(filename, 'r') as f:
        requirements =  f.readlines()
        requirements = [req.replace ("\n", "") for req in requirements ]

        if HYPHEN_E_DOR in requirements:
            requirements.remove(HYPHEN_E_DOR)
    return requirements



setup(
    name='hmlmddosd2dapp',
    version='0.0.1',
    author='Harshitaa',
    author_email='harshitaay@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)