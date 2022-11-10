# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Group, Match, Click, Drag, Screen, ScratchPad, DropDown
from libqtile import hook, layout, bar, widget
from libqtile.lazy import lazy
import subprocess
import os
import asyncio

#  _____                           
# |  __ \                          
# | |  \/_ __ ___  _   _ _ __  ___ 
# | | __| '__/ _ \| | | | '_ \/ __|
# | |_\ \ | | (_) | |_| | |_) \__ \
#  \____/_|  \___/ \__,_| .__/|___/
#                       | |        
#                       |_|  

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group(
        "9",
        matches=[Match(wm_class=["discord"])],
    ),
    Group(
        "0",
        matches=[Match(wm_class=["spotify", "Spotify"])],
        screen_affinity=None, # TODO
    )
]

#  _   __               
# | | / /               
# | |/ /  ___ _   _ ___ 
# |    \ / _ \ | | / __|
# | |\  \  __/ |_| \__ \
# \_| \_/\___|\__, |___/
#              __/ |    
#             |___/     

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
    Key([mod, "shift"], "r", lazy.reload_config(), lazy.spawn("notify-send \"Reload\""), desc="Reload the config"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),

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
    Key(["shift"], "Print", lazy.spawn("/usr/bin/scrot -s " + os.path.expanduser("~/Pictures/Screenshots/%Y-%m-%d_%H:%I:%S-screenshot.png")), desc="Take a screenshot"),
    Key(["control"], "Print", lazy.spawn("/usr/bin/scrot -u " + os.path.expanduser("~/Pictures/Screenshots/%Y-%m-%d_%H:%I:%S-screenshot.png")), lazy.spawn("notify-send \"Screenshot saved to ~/Pictures/Screenshots/...\""), desc="Take a screenshot"),

    # Blur
    Key([mod], "b", lazy.spawn(os.path.expanduser("~/.config/i3/scripts/blur-lock")), desc="Lock"),
    
    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master toggle"), desc="Mute Volume"),
    # Not Working Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5+"), desc="Higher Volume"),
    # Not working Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5-"), desc="Lower Volume"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("python " + os.path.expanduser("~/.config/qtile/scripts/brightness.py -d up")), desc="Brightness Up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("python " + os.path.expanduser("~/.config/qtile/scripts/brightness.py -d down")), desc="Brightness Down"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )
# Scratchpads

groups.extend(
    [
        ScratchPad("scratchpad", [
            DropDown("term", "pavucontrol", opacity=1),
        ]),
    ],
)

keys.extend(
    [
        Key([mod], 'F1', lazy.group['scratchpad'].dropdown_toggle('term')),
    ],
)

# Hooks

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.client_new
async def move_spotify(client):
    await asyncio.sleep(0.01)

    if client.name == 'Spotify':
        client.cmd_togroup(group_name="0")

# Layouts

layouts = [
    layout.Columns(
        border_normal="#383c4a",
        border_focus="#b782da",
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=2,
        border_on_single=True,
        margin=4,
        margin_on_single=4,
        insert_position=1,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="main.py"),
    ]
)

# ___  ___                     
# |  \/  |                     
# | .  . | ___  _   _ ___  ___ 
# | |\/| |/ _ \| | | / __|/ _ \
# | |  | | (_) | |_| \__ \  __/
# \_|  |_/\___/ \__,_|___/\___|

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Screens

screens = [
    Screen(
        top=bar.Gap(40),
    ),
]


auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = [] 
focus_on_window_activation = "focus"
follow_mouse_focus = True # Sometimes looses window focus when true
reconfigure_screens = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()