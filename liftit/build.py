from io import BytesIO

import os
from jinja2 import Environment, FileSystemLoader

import docker

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def create_container(config={}):
    env = Environment(
        loader=FileSystemLoader(THIS_DIR),
        trim_blocks=True
    )

    template = env.get_template('dockerfile.j2')

    dockerfile = template.render(image='nginx:alpine', commands=['echo "test"'], ports=['8080'])

    f = BytesIO(dockerfile.encode('utf-8'))
    client = docker.APIClient(base_url='unix://var/run/docker.sock')

    print([line for line in client.build(
        fileobj=f, rm=True, tag='name/image:latest'
    )])
