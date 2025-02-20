from setuptools import setup, find_packages

setup(
    name="pyxelpalette",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Liste des dépendances, par exemple :
        # "numpy>=1.21.0",
    ],
    author="Ton Nom",
    author_email="yann.pouepau1@gmail.com",
    description="Une bibliothèque Python pour la création et la manipulation d'images pixel art.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yxoro/PyxelPalette",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
