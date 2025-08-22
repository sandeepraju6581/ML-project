from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ML_project",
    version="0.1",
    author="sandeep raju",
    packages=find_packages(),
    install_requires=requirements,
)