from setuptools import setup

setup(name = 'printdescribe',
      version = '0.1.0',
      description = 'Print and describe',
      author='Okechukwu Okigbo',
      author_email='okigbookey@gmail.com',
      packages=['printdescribe'], 
      install_requires=['matplotlib',
                          'numpy',
                          'pandas'], 
      zip_safe = False)