from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='graynet_keras',
    version='0.1.1',
    description='Pretrained parameters for CT deep learning models.',
    license='MIT License',
    author='Paul Kim',
    url='https://github.com/MGH-LMIC/graynet_keras',
    packages=find_packages(),
    install_requires=install_requires
)
