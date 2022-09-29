#!/bin/sh

# Picom
picom -b --config ~/.config/picom/picom.conf & disown

# Polybar
~/.config/polybar/launch.sh & disown

# EOS Welcome
eos-welcome & disown

#get auth work with polkit-gnome
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown

# Screen Layout
~/.screenlayout/monitor.sh & disown

# Nitrogen
sleep 2 && nitrogen --restore & disown

# set powersavings for display:
xset s 480 dpms 600 600 600 & disown

# Desktop Notifications
dbus-launch dunst --config ~/.config/dunst/dunstrc & disown

# XSS-Lock
xss-lock -- /home/julian/.config/i3/scripts/blur-lock --transfer-sleep-lock -n & disown

# Dont know if these are needed

# dex --autostart --environment i3

#exec --no-startup-id blueberry-tray

# networkmanager-applet
#exec --no-startup-id nm-applet

# clipman-applet
#exec --no-startup-id xfce4-clipman