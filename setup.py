from distutils.core import setup


setup(
    name='dotenvpy',
    packages=['dotenvpy'],
    version='0.1.0',
    license='bsd-3-clause',
    description='Provides attribute-like read access to environment variables by wrapping python-dotenv',
    author='Alejandro de Haro',
    author_email='',
    url='https://github.com/adeharo9/dotenvpy',
    download_url='',
    keywords=['environment variables', 'deployments', 'settings', 'env',
              'dotenv', 'configurations', 'python'],
    install_requires=[
        'python-dotenv': ['python-dotenv>=0.14.0']
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ],
)
