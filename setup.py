from setuptools import find_packages, setup


setup(
    name="cotidia-doc",
    description="A documentation module for the Cotidia ecosystem.",
    version="1.0",
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://code.cotidia.com/cotidia/doc/",
    packages=find_packages(),
    package_dir={'doc': 'doc'},
    package_data={
        'cotidia.doc': [
            'templates/admin/doc/*.html',
            'templates/admin/doc/document/*.html',
        ]
    },
    namespace_packages=['cotidia'],
    include_package_data=True,
    install_requires=[
        'django>=1.10.2',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)
