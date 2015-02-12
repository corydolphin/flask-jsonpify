from setuptools import setup


setup(
    name='Flask-Jsonpify',
    version='1.5.0',
    url='https://github.com/CoryDolphin/flask-jsonpify',
    license='MIT',
    author='Cory Dolphin',
    author_email='corydolph.in@gmail.com',
    description="A Flask extension adding a decorator for JSONP support",
    long_description=open('README.rst').read(),
    py_modules=['flask_jsonpify'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    tests_require=['Flask-Testing', 'nose'],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)