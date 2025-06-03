from setuptools import setup, find_packages

setup(
    name="booklibrary",
    version="0.1.0",
    description="A simple book library management system for testing CI pipelines",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
