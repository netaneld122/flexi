try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='flexi',
    version='1.0.0',
    install_requires=['click', 'path.py'],
    packages=['flexi'],
    url='https://bitbucket.org/netaneld122/flexi',
    license='GPL License',
    author='Netanel Dziubov',
    description='Flexible tree data structure serialization utility',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
