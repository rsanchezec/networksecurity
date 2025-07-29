'''
El archivo setup.py es esencial para empaquetar y distribuir proyectos de Python. Lo utilizan setuptools 
(o distutils en versiones anteriores de Python) para definir la configuración del proyecto, como sus metadatos, dependencias, etc.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Esta función devolverá una lista de requisitos.
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Raul Sanchez",
    author_email="raulec1982@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)