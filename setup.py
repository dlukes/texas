from setuptools import setup, find_packages

setup(
    name="texas",
    version="0.0",
    author="David Lukeš",
    author_email="dafydd.lukes@gmail.com",
    description="Scripts for the Texas Czech ELAN transcripts.",
    license="GNU GPLv3",
    url="https://github.com/dlukes/texas",

    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        txeaf=convert:cli
    """,
)
