#!/bin/sh

apt-get update

apt-get -y install git apt-utils gcc wget
apt-get -y install curl libcurl4-openssl-dev

apt-get -y install python3 python3-pip

apt-get -y install tmux

pip3 install pycurl flask

WORKDIR=$(pwd)

# Install bro

BRO_DEB_PATH="http://download.opensuse.org/repositories/network:/bro/xUbuntu_14.04/"
BRO_APT_FILE="/etc/apt/sources.list.d/bro.list"

sh -c "echo \'deb $BRO_DEB_PATH /\' > $BRO_APT_FILE"

wget http://download.opensuse.org/repositories/network:bro/xUbuntu_14.04/Release.key
apt-key add — < Release.key
rm Release.key

apt-get update
apt-get -y install bro

# Install demo applications

git clone https://github.com/emiapwil/demo-http tutorial-sc16
make -C tutorial-sc16

export PATH=$PATH:$WORKDIR/tutorial-sc16/

# Install the mininet script
