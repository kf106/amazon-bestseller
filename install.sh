#!/bin/bash
# (C) 2019 Keir Finlow-Bates
# See LICENSE for the licensing details of this software

if [ -z $BASH_VERSION ] ; then
	echo -e "You must run this script using bash." 1>&2
	exit 1
fi


# Make sure we are running as root
if [[ $EUID -ne 0 ]]; then
	echo -e "This script must be run as root." 1>&2
	exit 1
fi

# uncomment for debug info
# set -x

# do the usual apt-get update
apt-get update

# BUG: remove pkg-resources line in requirements.txt if it exists
#     https://stackoverflow.com/questions/39577984/what-is-pkg-resources-0-0-0-in-output-of-pip-freeze-command
sed -i '/pkg-resources==0.0.0/d' ./requirements.txt

# install venv
apt-get install python3-venv

# this creates a copy of the python3 environment in a folder called venv
python3 -m venv venv

# this activates the virtual python3 environment
source venv/bin/activate

# needs the wheel package first
pip install wheel

# and this now installs all the packages needed for the project in venv
pip install --upgrade -r requirements.txt

# when your project is complete use
# $ pip freeze > requirements.txt
# to make sure the requirements are up to date and the right packages are installed
# To upgrade all pip packages run
# $ pip freeze |sed -ne 's/==.*//p' |xargs pip install -U --

echo -e ""
echo -e "--------------------------------------------------------------------------------"
echo -e "Required packages installed                                            "
echo -e "--------------------------------------------------------------------------------"
echo -e ""














