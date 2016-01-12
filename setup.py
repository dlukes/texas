from setuptools import setup

setup(
    name="texas",
    version="0.0",
    py_modules=["convert"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        txeaf=convert:cli
    """
)
