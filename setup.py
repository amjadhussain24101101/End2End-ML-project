from setuptools import setup, find_packages

setup(

    name ='mlproject',
    version ='0.0.1',
    author='Amjad Hussain',
    author_email='engramjad.hu@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','scikit-learn','seaborn','matplotlib']
)