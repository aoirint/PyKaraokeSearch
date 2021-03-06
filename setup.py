from setuptools import setup, find_packages
from typing import (
    List,
)

from PyKaraokeSearch import __VERSION__ as VERSION

install_requires: List[str] = [
    # dependencies like requirements.txt
    # 'numpy>=1.20.2', # https://pypi.org/project/numpy/
]

setup(
    name='PyKaraokeSearch',
    version=VERSION, # '0.1.0-alpha', # == 0.1.0-alpha0 == 0.1.0a0
    # license='MIT',

    # packages=[ 'PACKAGE_NAME', ],
    packages=find_packages(),
    include_package_data=True,

    # entry_points = {
    #     'console_scripts': [
    #         # create `main` function in PACKAGE_NAME/scripts/my_command_module.py
    #         'my_command_name = PACKAGE_NAME.scripts.my_command_module:main',
    #     ],
    # },

    install_requires=install_requires,

    author='aoirint',
    author_email='aoirint@gmail.com',

    url='https://github.com/aoirint/PyKaraokeSearch',
    description='Integrated karaoke search',

    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 3 - Alpha',
        # 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
