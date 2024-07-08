from setuptools import setup, find_packages

setup(
    name="SauceFramework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    include_package_data=True,
)
