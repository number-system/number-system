from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="numbersystem", # Replace with your own username
    version="0.1.3",
    author="Ritul Singh",
    author_email="ritulsingh00@gmail.com",
    description="This is a python library that converts the decimal number in binary, octal, and hexadecimal or vice versa.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/number-system",
    packages=['numbersystem'],
    inatall_requires=[],
    licence='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.6',
    keywords='numbersystem',
)