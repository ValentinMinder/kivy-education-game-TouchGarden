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

# copy start file on desktop for easy access
cp garden/start.sh start.sh
chmod u+x start.sh
chmod u+x garden/update.sh

# copy auto-start script in place (home folder, name '.gnomerc' and executable)
cp garden/autostart.sh ~/.gnomerc
chmod u+x ~/gnomerc

# should set delay of screen disabling to 'never' (no delay) 
gsettings set org.gnome.desktop.session idle-delay 0
# disable screen locking
gsettings set org.gnome.desktop.screensaver lock-enabled  false
# no lock
gsettings set org.gnome.desktop.screensaver lock-delay 0
#disable screen diming
gsettings set org.gnome.settings-daemon.plugins.power idle-dim false

# change background image
gsettings set org.gnome.desktop.background picture-uri file:///home/touchgarden/Desktop/garden/images/fond/wallpaper.png
