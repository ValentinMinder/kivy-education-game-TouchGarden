#!/bin/sh

# linux computers are setup with admin username:touchgarden and password: touchgarden
# Ubuntu 16.04.2 LTS Long Term Support is installed and supported until April 2021
# run this script with 'sh setup.sh' (sudo admin password is then asked, don't do 'sudo su' as this change to root user, and so things needs to be done as main touchgarden user)

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
chmod u+x ~/.gnomerc

# THESE LINES ARE ALSO IN UPDATE.SH
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

# TODO: setting up rtcwake and cron AS ROOT USER (for automated shutdown and restart), execute:
## sudo -su
## crontab -e
# choose nano and add the following line with ##

# everyday at 17:45 shutdown and programm restart at 9:45 the next day (16h later)
# min hour day-of-month month day-of-week(0-6) command
# every day from march-october, schedule restart on tomorrow at 9:45 (16 * 3600)
# computer in save-to-disk state (option 'disk') known as 'veille prolongée'
# computer will restart ONLY if shut down automatically with rtcwake
## 45 17 * 3-10 * sudo killall elousbd & sudo rtcwake -m disk -s 57600

# everyday from november-february, schedule a complet stop at midnight
# computer won't restart until manually power on
## 59 23 * 11-2 * sudo shutdown


# TODO: in file manager (nautilus), Edit > Preferences > Behavior > Single click to activate items + run executable files

# TODO: install driver from archive SW602479_Elo_Linux_ST_USB_Driver_v4.3.1_x86_64.zip
# follow guidelines at Elo-Linux-ST-USB-Driver-v4.3.1_Installation-Instructions.txt

# to re-calibrate, execute the following
# cd /etc/opt/elo-usb
# sudo ./elova --nvram

# to disable beep sound, execute the following
# cd /etc/opt/elo-usb
# sudo ./cplcmd
# then type 6, enter, y, enter, 0, enter
