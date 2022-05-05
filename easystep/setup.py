from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'EasyStep'
LONG_DESCRIPTION = 'RaspberryPi Stepper Motor Control Library'


setup(

        name="easystep", 
        version=VERSION,
        author="Deniz Erdogan",
        author_email="derdogan18@ku.edu.tr",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[]
)