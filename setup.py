from setuptools import find_packages, setup
from typing import List

setup(
  name='sensor',
  version='0.0.1',
  author="Yash",
  author_email="yashsuri1999@gmail.com",
  packages=find_packages(),
  intall_requires=["pymongo"]
)