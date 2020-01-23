import io

import setuptools


with io.open("README.md", "r") as fd:
    long_description = fd.read()


setuptools.setup(
    name="jigi-cli",
    version="0.0.1",
    author="Thomas Da Costa",
    author_email="thomas.dacosta@backmarket.com",
    description="Jira and GitHub cli tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BackMarket/jigi-cli",
    scripts=["scripts/jigi"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["PyGithub==1.45", "requests==2.22.0", "appdirs==1.4.3", "ConfigArgParse==1.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
)
