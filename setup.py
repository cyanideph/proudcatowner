from setuptools import setup, find_packages

requirements = ["requests", "torpy", "lxml", "secmail", "colored", "bs4", "names", "fancy_text", "colorama", "typing", "websocket-client==0.58.0", "setuptools", "json_minify",
                "six", "websockets"]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="proudcatowner",
    license='MIT',
    author="",
    version="1.0.8",
    author_email="",
    description="",
    url="https://github.com/forevercynical/proudcatowner",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps'
    ],
    python_requires='>=3.6',
)
