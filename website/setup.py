"""website package configuration."""

from setuptools import setup

setup(
    name='website',
    version='0.1.0',
    packages=['website'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-DebugToolbar',
        'Flask-SQLAlchemy',
        'libsass',
        'PyMySQL',
        'flask_wtf'
    ],
    sass_manifests={
        'website': ('static/sass', 'static/css', '/static/css')
    }
)
