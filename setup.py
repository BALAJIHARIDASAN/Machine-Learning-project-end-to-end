from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"  # project name
VERSION="0.0.1"
AUTHOR="Balaji Haridasan"  # author name
DESRCIPTION="This is a first full scale Machine Learning Project"  # description about the project

REQUIREMENT_FILE_NAME="requirements.txt"  # reading the requirement file

HYPHEN_E_DOT = "-e ."  # to run all required packages for project


def get_requirements_list() -> List[str]:   # output of the file is list of string type like [numpy],[pandas],[sklearn]
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:  # open the file
        requirement_list = requirement_file.readlines()  #  read the file line by line
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:   # to remove hypen from the requriement.txt file
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list  



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(), 
install_requires=get_requirements_list() # to read the packages in the requirements.txt
)  