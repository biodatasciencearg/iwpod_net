from setuptools import find_packages, setup

setup(
    name='iwpodnet',
    packages=find_packages(),
    version='0.1',
    description='project to find license plates and fix distorsions',
    author='ELIASLOPEZ',
    license='MIT',
    package_data={'': ['weights/iwpod_net.json','weights/iwpod_net.h5']},
    include_package_data=True, 
    install_requires = ["opencv-python==4.8.1.78"
                        ,"numpy==1.23.5"]
    )