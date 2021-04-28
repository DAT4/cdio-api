from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    _license = f.read()

setup(
        name='CDIO card finder',
        version='0.0.1',
        description='Module to find a card in an image',
        long_description=readme,
        author='Gruppe 24',
        author_email='mail@mama.sh',
        url='cdio.mama.sh',
        licence=_license,
        packages=find_packages(),
)
