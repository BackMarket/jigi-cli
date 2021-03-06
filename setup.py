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
    install_requires=[
        "ConfigArgParse==1.0",
        "PyGithub==1.45",
        "appdirs==1.4.3",
        "jira==2.0.0",
        "requests==2.22.0",
        "tabulate==0.8.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    license="MIT",
)
