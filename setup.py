from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gemmolt",
    version="0.1.0",
    author="GemMolt Team",
    author_email="team@gemmolt.dev",
    description="Master Coding and Manager Assistant - Autonomous, secure central nervous system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Daisy1969/GemMolt",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0",
    ],
    extras_require={
        "gcp": [
            "google-cloud-secret-manager>=2.16.0",
            "google-cloud-iam>=2.12.0",
            "google-auth>=2.17.0",
        ],
        "dev": [
            "pytest>=7.3.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "gemmolt=gemmolt.cli:main",
        ],
    },
)
