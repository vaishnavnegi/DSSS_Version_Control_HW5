pip install setuptools
from setuptools import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='0.1.0',    
    description='DSSS HW5 Version Control',
    author='Vaishnav Negi',
    author_email='vaishnavnegi207@gmail.com',
    packages = find_packages(),
    install_requires=['mpi4py>=2.0',"numpy","turtle"],
    )
