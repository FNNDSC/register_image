from setuptools import setup

setup(name='imgreslice',
    version='1.0.0',
    description='A ChRIS plugin for image registration and reslicing.',
    author='FNNDSC / Arman Avesta, MD, PhD',
    author_email='dev@babyMRI.org',
    url='https://github.com/ArmanAvesta/image-reslice',
    py_modules=['app', 'register'],
    install_requires=['chris_plugin', 'FSL'],
    license='MIT',
    entry_points={'console_scripts': ['imgreslice = app:main']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'],
    extras_require={'none': [], 'dev': ['pytest~=7.1']})
