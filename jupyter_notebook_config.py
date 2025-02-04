c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook

# Notebook config

c.NotebookApp.allow_origin = '*' # put your public IP Address here
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
# ipython -c "from notebook.auth import passwd; passwd()" // Using this command to change password
# c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$/DJ3H3hTXpz6JW3P0rCmhw$wNOqs6zfdHwLMwqNQRIjbA'
c.NotebookApp.port = 8888
