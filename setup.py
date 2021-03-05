import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord-help", # Replace with your own username
    version="0.0.8a",
    author="Alex Hutz",
    author_email="frostiiflames@gmail.com",
    description="A package for discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/FrostiiWeeb/discord-help"
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)