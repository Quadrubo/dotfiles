#!bin/bash

# Install all pacman dependencies
sudo pacman -Syu --noconfirm code flatpak docker docker-compose python-pip xclip jq fish plank ttf-jetbrains-mono kitty 

# Install the system theme
mkdir ~/tmp
cd ~/tmp
git clone https://github.com/vinceliuice/Colloid-gtk-theme
cd Colloid-gtk-theme/
./install.sh -c dark -t purple -s compact -l --tweaks dracula normal rimless

# Yay installations
yay -S --noprovides --answerdiff None --answerclean None --mflags "--noconfirm" stylepak-git devilspie2 spicetify-cli update-grub
stylepak install-system Colloid-Purple-Dark-Compact-Dracula

# Python installations
python3 -m pip install python3-xlib

# Save git credentials
git config --global credential.helper /usr/lib/git-core/git-credential-libsecret

# Docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker julian

