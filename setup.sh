#!/bin/sh

# SETUP file to run only ONCE!
# update.sh is then created and run this one just to update the app
# from terminal: 'sh update.sh'

#install python (in case it's not shipped with unix version)
sudo apt-get --yes install python
python --version

#install git (in case it's not shipped with unix version)
sudo apt-get --yes install git
git --version
git config --global user.email "Valentin.Minder@users.noreply.github.com"
git config --global user.name "Valentin Minder"

#install kivy (REQUIRED) and all its dependency (SDL, OpenGL, etc)
sudo apt-get --yes install python-kivy

# clone the code source (for the first time)
cd ~/Desktop
git clone https://github.com/ValentinMinder/TouchGarden garden

# copy update and start files on desktop for easy access
cp garden/update.sh update.sh
cp garden/start.sh start.sh
chmod u+x update.sh
chmod u+x start.sh

