from setuptools import setup

setup(
    name='mimicry-hiive',
    version='0.3.0',
    author='M. Simpson, J. McGehee',
    author_email= 'mjs2600@gmail.com, jlmcgehee21@gmail.com',
    packages=['mimicry'],
    license='MIT', #Unless you prefer another
    description='MIMIC Randomized Optimization Algorithm in Python',
    long_description='MIMIC Randomized Optimization Algorithm in Python',
    install_requires=['numpy', 'scipy', 'scikit-learn', 'pandas', 'networkx', 'matplotlib'],
    python_requires='>=3',
    zip_safe=False
)
