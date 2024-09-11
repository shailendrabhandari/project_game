from setuptools import setup, find_packages

setup(
    name="ACIT_GAME_Module",  # The package name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="A fun game module as a part of ACIT4420 the lecture series. Basically from Lecture 5, 6, and 7.",
    author="Shailendra Bhandari",
    author_email="shailendra.bhandari@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'games=games.main:main',  # Points directly to the main function in main.py
        ],
    },
)

