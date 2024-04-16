from setuptools import find_packages, setup

setup(
    name='iwpodnet',
    packages=find_packages(),
    version='0.1',
    description='project to find license plates and fix distorsions',
    author='ELIASLOPEZ',
    license='MIT',
    install_requires = ["keras==2.15.0"
                        ,"opencv-python==4.8.1.78"
                        ,"numpy==1.23.5"
                        , "tensorflow==2.15.0"]
)