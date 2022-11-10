# dotfiles

<details>
<summary>
My Cinnamon Theme (Active)
</summary>

## My Cinnamon Theme (Active)

These dotfiles use the EndeavourOS Cinnamon edition and are untested on everything else. 

### Workspaces

Set the number of workspaces to 10 by default.

```shell
gsettings set org.cinnamon.desktop.wm.preferences num-workspaces 10
```

### Cinnamon Backup

To restore the cinnamon backup use dconf.

```shell
dconf load /org/cinnamon/ < cinnamon_backup
```

</details>

<details>
<summary>My i3 Theme (Inactive)</summary>

## My i3 Theme (Inactive)

### Scroll Direction

```console
cp /usr/share/X11/xorg.conf.d/30-touchpad.conf /etc/X11/xorg.conf.d
```

Get the Device name from `xinput list`.

Edit `/etc/X11/xorg.conf.d/30-touchpad.conf`.
```conf
Section "InputClass"
    ...
    Identifier "{device_name}"
    Option "NaturalScrolling" "on"
    MatchIsTouchpad "on"
EndSection
```

### Polybar

#### Base Requirements
```console
sudo pacman -S polybar
sudo pacman -S ttf-font-awesome
sudo pacman -S ttf-jetbrains-mono
```

#### Spotify Integration
```console
yay -S polybar-spotify-module
systemctl --user enable spotify-listener
systemctl --user start spotify-listener
```

#### Config Files
```console
chmod +x ~/.config/polybar/launch.sh
```

### Kitty

```console
sudo pacman -S kitty
```

### I3

#### Requirements

```console
yay -S autotiling
sudo pacman -S xss-lock
yay -S i3lock-color
```
#### Brightness

```console
sudo usermod -aG video {user}
newgrp video
```

Edit `/etc/udev/rules.d/backlight.rules`.
```rules
KERNEL=="amdgpu_bl0", SUBSYSTEM=="backlight", RUN+="/bin/chgrp video /sys/class/backlight/amdgpu_bl0/brightness"
KERNEL=="amdgpu_bl0", SUBSYSTEM=="backlight", RUN+="/bin/chmod g+w /sys/class/backlight/amdgpu_bl0/brightness"
```

```console
sudo udevadm control --reload
sudo udevadm trigger
```
#### Screenshots

```console
mkdir ~/Pictures/Screenshots
```

### firefox theme

`about:debugging#/runtime/this-firefox`
- Load temporary Addon

### Get lock working

`/etc/systemd/logind.conf`

`HandleLidSwitch=lock`

### Bluetooth

`sudo systemctl enable bluetooth.service`
</details>