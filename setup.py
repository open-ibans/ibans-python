from setuptools import setup, find_packages

setup(
    name="ibans",
    version="0.0.1",
    url="https://github.com/iltoningui/ibans-py",
    author="Ilton Ingui",
    author_mail="iltoningui@outlook.com",
    description="Parses Iban and Swift/BIC",
    description_long=open("README.rst").read(),
    packages=find_packages("ibans"),
    package_dir={'': 'ibans'},
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    package_data={'txt': ['data/*.txt']},
)
