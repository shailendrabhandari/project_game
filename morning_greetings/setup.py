# setup.py

from setuptools import setup, find_packages

setup(
    name='morning_greetings',
    version='1.0',
    packages=find_packages(),
    description='A package to automate sending Good Morning messages.',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'morning-greetings=morning_greetings.main:main',
        ],
    },
)

