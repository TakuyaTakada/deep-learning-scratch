from setuptools import setup, find_packages
import deepl_scratch

NAME = 'deepl-scratch'
DESCRIPTION = 'deepl-scratch'
AUTHOR = 'Takuya Takada'
AUTHOR_EMAIL = 'takuya.takada00@gmail.com'
URL = 'https://github.com/TakuyaTakada/deep-learning-scratch'
DOWNLOAD_URL = 'https://github.com/TakuyaTakada/deep-learning-scratch'
VERSION = deepl_scratch.__version__
PYTHON_REQUIRES = '>=3.9'

INSTALL_REQUIRES = [
    'numpy>=1.23.1'
]

EXTRA_REQUIRES = []

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    download_url=DOWNLOAD_URL,
    version=VERSION,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extra_require=EXTRA_REQUIRES,
)
