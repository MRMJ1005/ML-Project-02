from setuptools import find_packages,setup
from typing import List

con='-e .'

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if con in requirements:
            requirements.remove(con)

    return requirements




setup(
name='MLProject 02',
version='0.0.1',
author='Mazhar',
author_email='syedmazharhussain2607@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)