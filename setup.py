import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='overload',
    version='0.0.1',
    author='jemand2001',
    author_email='jmand@gmx.de',
    description='a small implementation of the @overload decorator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jemand2001/overload',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8'
)
