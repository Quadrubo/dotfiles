from distutils.spawn import spawn
from libqtile.lazy import lazy
from libqtile.config import Key
import os

mod = "mod4"
terminal = "kitty"
browser = "firefox"
files = "/usr/bin/thunar"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus to up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Rofi
    Key([mod], "d", lazy.spawn("rofi -modi drun -show drun -config ~/.config/rofi/rofidmenu.rasi"), desc="Show apps"),
    Key([mod], "t", lazy.spawn("rofi -show window -config ~/.config/rofi/rofidmenu.rasi"), desc="Show windows"),
    # TODO scripts folder seperate
    Key([mod, "shift"], "e", lazy.spawn(os.path.expanduser("~/.config/i3/scripts/powermenu")), desc="Open powermenu"),
    # TODO not working Key([mod], "F1", lazy.spawn(os.path.expanduser("~/.config/i3/scripts/keyhint-2")), desc="Spawn keyhitns"),
    Key([mod, "shift"], "p", lazy.spawn(os.path.expanduser("~/.config/i3/scripts/power-profiles")), desc="Open power profiles"),

    # TODO bindsym $mod+Shift+n exec ~/.config/i3/scripts/empty_workspace
    # TODO bindsym XF86AudioRaiseVolume exec amixer -D pulse sset Master 5%+ && pkill -RTMIN+1 i3blocks
    # TODO bindsym XF86AudioLowerVolume exec amixer -D pulse sset Master 5%- && pkill -RTMIN+1 i3blocks
    # TODO bindsym $mod+XF86AudioRaiseVolume exec amixer -D pulse sset Master 1%+ && pkill -RTMIN+1 i3blocks
    # TODO bindsym $mod+XF86AudioLowerVolume exec amixer -D pulse sset Master 1%- && pkill -RTMIN+1 i3blocks

    # mute
    # TODO bindsym XF86AudioMute exec amixer sset Master toggle && killall -USR1 i3blocks

    # audio control
    # TODO bindsym XF86AudioPlay exec playerctl play
    # TODO bindsym XF86AudioPause exec playerctl pause
    # TODO bindsym XF86AudioNext exec playerctl next
    # TODO bindsym XF86AudioPrev exec playerctl previous

    # Apps
    Key([mod], "w", lazy.spawn(browser), desc=f"Open browser"),
    Key([mod], "n", lazy.spawn(files), desc=f"Open files"),

    # Screenshots
    Key([], "print", lazy.spawn("/usr/bin/scrot " + os.path.expanduser("~/Pictures/Screenshots/%Y-%m-%d_%H:%I:%S-screenshot.png")), lazy.spawn("notify-send \"Screenshot saved to ~/Pictures/Screenshots/...\""), desc="Take a screenshot"),
    Key(["shift"], "Print", lazy.spawn("/usr/bin/scrot -s " + os.path.expanduser("~/Pictures/Screenshots/%Y-%m-%d_%H:%I:%S-screenshot.png")), lazy.spawn("notify-send \"Screenshot saved to ~/Pictures/Screenshots/...\""), desc="Take a screenshot"),
    Key(["control"], "Print", lazy.spawn("/usr/bin/scrot -u " + os.path.expanduser("~/Pictures/Screenshots/%Y-%m-%d_%H:%I:%S-screenshot.png")), lazy.spawn("notify-send \"Screenshot saved to ~/Pictures/Screenshots/...\""), desc="Take a screenshot"),


    Key([mod], "b", lazy.spawn(os.path.expanduser("~/.config/i3/scripts/blur-lock")), desc="Lock"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("python " + os.path.expanduser("~/.config/qtile/scripts/brightness.py -d up")), desc="Brightness Up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("python " + os.path.expanduser("~/.config/qtile/scripts/brightness.py -d down")), desc="Brightness Down"),
]