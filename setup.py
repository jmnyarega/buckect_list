from setuptools import setup,find_packages

setup(
    name='Bucket list',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.2',
        'SQLAlchemy>=0.6'
    ]
)