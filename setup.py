import os

from setuptools import setup, find_packages
from treeadmin import __version__ as version

setup(
    name = 'django-treeadmin',
    version = version,
    description = 'Tree UI for mptt-managed models, extracted from FeinCMS',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = 'Matthias Kestenholz  et al.',
    author_email = 'mk@spinlock.ch',
    url = 'https://www.github.com/piquadrat/django-treeadmin',
    packages = find_packages(),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.2',
        'django-mptt>=0.5',
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
