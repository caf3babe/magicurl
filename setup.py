import os
from setuptools import setup, find_packages
from magicurl import __version__
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "magicurl",
    version = __version__,
    author = "Prateek Khushalani",
    author_email = "prateek.khushalani@gmail.com",
    description = ("A tool for creating short and simple URL's for complex ones"),
    keywords = "magicurl tinyurl url shortner",
    url = "https://github.com/prateek2408/magicurl",
    packages=find_packages(),
    package_data={'magicurl': ['config/murl.yaml']},
    install_requires=["flask==1.1.2"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: Alpha",
        "Topic :: Utility"
    ],
    entry_points = {
        'console_scripts': [
            'magicurl = magicurl.main.invoke:start_server'],
        },
)
