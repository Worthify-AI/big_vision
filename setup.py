from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="big_vision",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/your_repo_name",
    packages=find_packages('.'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here
    ],
)
