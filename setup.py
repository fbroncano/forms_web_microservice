# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="SurveyUp: Forms Web",
    author_email="fbroncano@unex.es",
    url="",
    keywords=["Swagger", "SurveyUp: Forms Web"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API del microservicio _Forms Web_ del proyecto _SurveyUp_ de la asignatura Ingeniería de Servicios TIC del Master  Universitario de Ingeniería Informática de la EPCC del curso 2024/2025.
    """
)
