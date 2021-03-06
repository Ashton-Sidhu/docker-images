from IPython import get_ipython
ipython = get_ipython()

# If in ipython, load autoreload extension
if "ipython" in globals():
	ipython.magic("load_ext autoreload")
	ipython.magic("autoreload 2")
	ipython.magic("load_ext autotime")
