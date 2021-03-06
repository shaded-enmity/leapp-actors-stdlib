import json
import os


import click


@click.command('new-project')
@click.argument('name')
def cli(name):
    basedir = os.path.join('.', name)
    if not os.path.isdir(basedir):
        os.mkdir(basedir)
        project_dir = os.path.join(basedir, '.leapp')
        os.mkdir(project_dir)
        with open(os.path.join(project_dir, 'info'), 'w') as f:
            json.dump({
                'name': name,
                'channel_data': {}
            }, f)
        print "New project {} has been created in {}".format(name, os.path.realpath(name))
