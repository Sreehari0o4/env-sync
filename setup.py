from setuptools import setup, find_packages

setup(
    name="envsync0o2",
    version="0.1.0",
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
    author="Sreehari S Kumar",
    description="A CLI tool to securely sync .env files across teams using encryption and GitHub Gists.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires=">=3.8",
)