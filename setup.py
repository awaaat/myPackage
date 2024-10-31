from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This is y first example package example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/awaaat/mypackage',
    author='allano',
    author_email='awaliaulah65@gmail.com'
)