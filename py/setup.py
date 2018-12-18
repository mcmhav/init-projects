from setuptools import setup, find_packages
import json

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

with open('package.json') as f:
  package = json.load(f)

setup(
  name=package['name'],
  version=package['version'],
  description=package['description'],
  long_description=readme,
  author='cake',
  author_email='mcmhav@gmail.com',
  url='https://github.com/mcmhav',
  license=license,
  packages=find_packages(exclude=('tests', 'docs'))
)
