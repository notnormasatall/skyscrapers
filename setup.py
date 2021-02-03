import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scyscrapers-rodzin",
    version="0.0.1",
    author="Taras Rodzin",
    author_email="taras.rodzin@ucu.edu.ua",
    description="A module for validating the board of symbols.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/notnormasatall/puzzle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.6',
)
