from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
      name='OpenMEASURE',
      version='0.0.1',
      description='Python package for soft sensing applications',
      py_modules=['sparse_sensing'],
      package_dir={'':'src'},
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=['numpy>=1.19', 'scipy>=1.5']
      )