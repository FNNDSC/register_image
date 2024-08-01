
from setuptools import setup

setup(name='register_image',
    version='1.0.0',
    description='A ChRIS plugin for image registration and re-slicing.',
    author='FNNDSC / Arman Avesta, MD, PhD',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/register_image',
    py_modules=['app', 'register'],
    install_requires=['chris_plugin', 'nipype', 'FSL'],  # ToDo: can I add FSL here like that?
    license='MIT',
    entry_points={'console_scripts': ['register_image = app:main']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'],
    extras_require={'none': [], 'dev': ['pytest~=7.1']})
