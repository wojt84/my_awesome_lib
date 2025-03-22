from setuptools import setup, find_packages

setup(
    name="my_awesome_lib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  
    include_package_data=True,
    description="A lightweight Python library for data, math, and text processing.",
    author="Wojciech",
    author_email="wsobcz@gmail.com",
    url="https://github.com/wojt84/my_awesome_lib",  
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
)
