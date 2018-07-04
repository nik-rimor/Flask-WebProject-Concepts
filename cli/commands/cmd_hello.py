import subprocess

import click

@click.command()
@click.option('--name/--no-name', default=True,
    help='Accepts the name to greet you with')
@click.argument('fname', default='Spyros')
def cli(name, fname):
    """
    Run hello to greet you with a name.

    :param name: Accepts a name to greet you with
    :oaram fname: FirstName given for greeting
    :return: A greeting string
    """
    hello_flag_name = ''

    if name:
        hello_flag_name = fname
    
    cmd = "echo hello {0}".format(hello_flag_name)
    return subprocess.call(cmd, shell=True)