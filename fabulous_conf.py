import os.path

fabconf = {}

#  Do not edit
fabconf['FABULOUS_PATH'] = os.path.dirname(__file__)

# Hostname for production instance -- to add in /etc/hosts
fabconf['SERVER_PRODUCTION_HOSTNAME'] = "ejrf-server"

# Hostname for staging instance -- edit /etc/hosts
fabconf['SERVER_STAGING_HOSTNAME'] = "ejrf-test-server"

# Username for connecting to instaces
fabconf['SERVER_USERNAME'] = "ejrf"

# Domain name
fabconf['DOMAIN_NAME'] = "app.ejrf"

# User home path
fabconf['DOMAIN_HOME'] = "/home/ejrf"

# Current Path
fabconf['CURRENT_PATH'] = "%s/app/src" % fabconf['DOMAIN_HOME']

# Releases Path
fabconf['RELEASES_PATH'] = "%s/releases" % fabconf['DOMAIN_HOME']

# Shared path
fabconf['SHARED_PATH'] = "%s/shared" % fabconf['DOMAIN_HOME']

# GIT URL
fabconf['GIT_URL'] = "https://github.com/eJRF/ejrf"

# Env file
fabconf['ENV_FILE'] = "pip-requirements.txt"

# Full local path for .ssh
fabconf['SSH_PATH'] = "~/.ssh"

# Project name: polls
fabconf['PROJECT_NAME'] = "ejrf"

# Where to install apps
fabconf['APPS_DIR'] = fabconf['DOMAIN_HOME']

# Where you want your project installed: /APPS_DIR/PROJECT_NAME
fabconf['PROJECT_PATH'] = fabconf['CURRENT_PATH']

# App domains
fabconf['DOMAINS'] = "ejrf.com www.ejrf.com"

# Path for virtualenvs
fabconf['VIRTUALENV_DIR'] = "/home/ejrf/app/venv"

# Path for pip
fabconf['PIP_PATH'] = "/home/ejrf/app/venv/bin/pip"

# Email for the server admin
fabconf['ADMIN_EMAIL'] = "unicef-ejrf@thoughtworks.com"

# Git username for the server
fabconf['GIT_USERNAME'] = "ejrf-server"

# Name of the private key file used for github deployments
fabconf['GITHUB_DEPLOY_KEY_NAME'] = "id_rsa"

# Don't edit. Local path for deployment key you use for github
fabconf['GITHUB_DEPLOY_KEY_PATH'] = "%s/%s" % (fabconf['SSH_PATH'], fabconf['GITHUB_DEPLOY_KEY_NAME'])

# Path to the repo of the application you want to install
fabconf['GITHUB_REPO'] = "https://github.com/eJRF/ejrf"

# Virtualenv path
fabconf["VENV_PATH"] = "/home/ejrf/app/venv"

# Virtualenv activate command
fabconf['ACTIVATE'] = "source %s/bin/activate" % fabconf['VENV_PATH']

# Name tag for your server instance
fabconf['INSTANCE_NAME_TAG'] = "ejrf Server"
