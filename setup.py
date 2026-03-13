from setuptools import setup, find_packages

setup(
    name="envsync",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "python-dotenv",
        "cryptography",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "envsync=envsync.cli:cli"
        ]
    },
)