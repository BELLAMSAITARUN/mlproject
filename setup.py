from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # Iterate through the list and remove lines equal to "-e ."
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author="BELLAMSAITARUN",
    author_email="19211a0310@bvrit.ac.in",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
