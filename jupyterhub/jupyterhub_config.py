import os
import sys

# Authentication
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.bind_dn_template = ["uid={username},cn=users,cn=accounts,dc=sidhulabs,dc=ca"]
c.LDAPAuthenticator.server_address = os.environ['LDAP_SERVER_ADDRESS']
c.LDAPAuthenticator.allowed_groups = [
    "cn=jupyter,cn=groups,cn=accounts,dc=sidhulabs,dc=ca",
]

c.Authenticator.admin_users = os.environ["ADMIN_USERS"].split(",")

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']

# https://jupyterlab.readthedocs.io/en/stable/user/jupyterhub.html
# c.DockerSpawner.cmd=["jupyter-labhub"]
c.JupyterHub.hub_connect_ip = os.environ['HUB_IP']
c.JupyterHub.hub_ip = "127.0.0.1"

# For debugging
# c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
# c.DummyAuthenticator.password = ""

c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': [sys.executable, 'cull_idle_servers.py', '--timeout=42000']
    },
]

c.Spawner.default_url = '/lab'

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {
    '/home/sidhu': notebook_dir,
    '/opt/mlruns': '/opt/mlruns'
}
c.DockerSpawner.debug = True
c.DockerSpawner.start_timeout = 180
