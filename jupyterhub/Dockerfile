FROM jupyterhub/jupyterhub:1.4

# Copy the JupyterHub configuration in the container
COPY jupyterhub_config.py .

# Download script to automatically stop idle single-user servers
COPY cull_idle_servers.py .

# Install dependencies (for advanced authentication and spawning)
RUN pip install dockerspawner jupyterhub-ldapauthenticator
