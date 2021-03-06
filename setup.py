# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


readme = open('README.md').read()

setup(
    name='Marmitek-Gw',
    version='1.2.4',
    description=('A gateway to use the marmitek sensors'),
    long_description=readme,
    author='Clément Pallière, Romain Endelin',
    author_email='romain.endelin@mines-telecom.fr',
    url='https://github.com/pawmint/marmitek-gw',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'UbiGate>=0.2.3'
    ],
    dependency_links=[
        "git+ssh://git@github.com/pawmint/ubiGATE.git@v0.2.3#egg=UbiGate-0.2.3"
    ],
    entry_points = {
        'console_scripts': ['marmitek-gw=marmitek.gateway:main'],
    },
    license='Copyright',
    zip_safe=True,  # To be verified
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Environment :: Console',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering',
    ],
)
