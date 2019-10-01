from setuptools import setup

setup(
    name='mimicry-hiive',
    version='0.3.0',
    author='M. Simpson, J. McGehee',
    author_email= 'mjs2600@gmail.com, jlmcgehee21@gmail.com',
    packages=['mimicry'],
#     scripts=['bin/example1.py','bin/example2.py'], #Any scripts we may want
#     url='http://pypi.python.org/pypi/mimicry/', #If we actually want to upload this to PyPI
    license='MIT', #Unless you prefer another
    description='MIMIC Randomized Optimization Algorithm in Python',
    long_description='MIMIC Randomized Optimization Algorithm in Python',
    install_requires=['numpy', 'scipy', 'scikit-learn', 'pandas', 'networkx', 'matplotlib'],
    python_requires='>=3',
)
