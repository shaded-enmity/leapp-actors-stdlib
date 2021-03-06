from setuptools import setup

setup(
    name='leapp-actor-standard-library',
    py_modules=['leapp.actors', 'leapp.models', 'leapp.channels', 'leapp.tool'],
    install_requires=['click', 'marshmallow'],
    entry_points='''
        [console_scripts]
        actor-tool=leapp.tool:main
    '''
)