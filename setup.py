from setuptools import setup, find_packages

setup(
    name='ducttape',
    version='0.1',
    url='http://github.com/adamrt/ducttape/',
    license='ISC',
    author='Adam Patterson',
    author_email='adam@adamrt.com',
    description='Server deployment tools based on fabric.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'fabric',
        'jinja2'
    ],
)
