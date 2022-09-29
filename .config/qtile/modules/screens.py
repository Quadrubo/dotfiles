from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Gap(40),
        # bottom=bar.Bar(
        #     [
        #         widget.CurrentLayout(),
        #         widget.GroupBox(),
        #         widget.Prompt(),
        #         widget.WindowName(),
        #         widget.Chord(
        #             chords_colors={
        #                 "launch": ("#ff0000", "#ffffff"),
        #             },
        #             name_transform=lambda name: name.upper(),
        #         ),
        #         widget.TextBox("default config", name="default"),
        #         widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        #         # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        #         # widget.StatusNotifier(),
        #         widget.Systray(),
        #         widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        #         widget.QuickExit(),
        #     ],
        #     24,
        #     # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        #     # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # ),
    ),
]