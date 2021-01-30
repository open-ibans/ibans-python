from setuptools import setup, find_packages

with open("README.rst", 'r') as f:
    long_description = f.read()
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f]


setup(
    name="ibans",
    version="1.0.0",
    url="https://github.com/iltoningui/ibans-python",
    author="Ilton Ingui",
    author_mail="iltoningui@outlook.com",
    description="Parses Iban and Swift/BIC",
    long_description=long_description,
    long_description_type='text/x-rst',
    packages=find_packages("ibans"),
    package_dir={'': 'ibans'},
    python_requires='>=3.6',
    license='MIT',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Office/Business :: Financial',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=True,
    package_data={'txt': ['data/*.txt']},
)
