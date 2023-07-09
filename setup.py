from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="kaiten",
    version="1.0.0",
    author="Xitroy",
    author_email="ymh9w@yandex.ru",
    description="Python Kaiten API client for convenient work with it",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Xitroy/Kaiten/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)