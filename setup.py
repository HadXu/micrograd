import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="micrograd",
    version="0.1.0",
    author="hadxu",
    author_email="hadxu123@gmail.com",
    description="Autograd",
    readme=readme,
    readme_type="text/markdown",
    url="https://github.com/hadxu/micrograd",
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
