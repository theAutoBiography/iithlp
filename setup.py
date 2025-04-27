from setuptools import setup, find_packages

setup(
    name="iithlp",
    version="0.2.3",
    author="Ramanan S",
    author_email="ramanan93@gmail.com",
    description="A comprehensive transliteration scheme for Indian languages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/theAutoBiography/iithlp",
    packages=find_packages() ,
    include_package_data=True,
    package_data={
        "iithlp": ["data/mappings/*.json"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    test_suite="tests",
)
