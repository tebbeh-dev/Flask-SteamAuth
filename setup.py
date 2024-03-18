from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Flask-SteamAuth',
    version='0.1.0',
    author='tebbeh',
    description='A Flask extension for Steam authentication',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tebbeh-dev/flask-steamauth',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
