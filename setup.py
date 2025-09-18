from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt if it exists
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="liquid-s4",
    version="0.1.0",
    description="Liquid Structural State-Space Models",
    author="Liquid-S4 Authors",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.9.0",
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "hydra-core>=1.1.0",
        "omegaconf>=2.1.0",
        "einops>=0.4.0",
        "opt-einsum>=3.3.0",
    ] + read_requirements(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
