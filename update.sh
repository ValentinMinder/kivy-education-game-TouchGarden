#!/bin/sh

# update the source code from latest online release
cd ~/Desktop/garden
git pull


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
