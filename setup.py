from setuptools import find_packages, setup
from typing import List

HYFEN_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
    
        if HYFEN_DOT in requirements : 
            requirements.remove(HYFEN_DOT)

    return requirements

setup(
name='ML_project',
version='0.0.1',
author='Yagnesh',
author_email='dave.1@iitj.ac.in',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)