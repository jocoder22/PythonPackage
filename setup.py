from setuptools import setup

setup(name = 'catanalysis',
      version = '0.1.0',
      description = 'Categorical Analysis',
      author='Okechukwu Okigbo',
      author_email='okigbookey@gmail.com',
      packages=['catanalysis'], 
      install_requires=['matplotlib',
                          'numpy',
                          'pandas'], 
      zip_safe = False)