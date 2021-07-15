# JupterHub


## Connecting to Jupyter Instance through JupyterHub

To connect to a Jupyter server running remotely on JupyterHub, follow these instructions:

Log-in to your JupyterHub

1. Go to the ‘Token’ page by clicking ‘Token’ in the top bar

![image](https://user-images.githubusercontent.com/9558507/125863808-31f5254a-3331-4a4a-bb3a-6e275b756cb4.png)

2. Type in a description for the new token you want, and click ‘Request new API Token’

![image](https://user-images.githubusercontent.com/9558507/125863918-c62d2dbb-db59-417a-ac6b-1f3cd10fe871.png)

3. Click `Request Token`

4. Copy your token and keep it somewhere safe. You should treat this like a password to your JupyterHub. You can (and should!) revoke it (as I have done) from the same page when you are no longer using it.

![image](https://user-images.githubusercontent.com/9558507/125863979-e4477a68-376f-4954-903d-4290d37e978d.png)

Construct your notebook server URL with the following template: `https://<your-hub-url>/user/<your-hub-user-name>/?token=<your-token>`. Note that your hub user name might sometimes be escaped from whatever you used to actually log in, if it has special characters. You can verify this by looking at the URL you get once you log in to your JupyterHub — it should have the right one after ‘user’.

5. Create or open a new notebook. The kernel for this should now live on your JupyterHub! You can verify this by running !hostname, which should return the hostname of your remote JupyterHub server instead of your local hostname. You can also try importing libraries that are in the remote JupyterHub server, but not your local file system.
Tada! That wasn’t so hard, was it?
