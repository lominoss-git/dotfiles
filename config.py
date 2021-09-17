###################################################
##################### My qTile ####################
###################################################

# Importing python/qtile libraries:

import os
import re
import socket
import subprocess
import os.path
from libqtile.config import Key, Screen, Group, Match, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer, base
from typing import List  # noqa: F401

# Set Default modkey:
mod = "mod4"

bar_size = 48

# Panel Bg, Date & Time Fg, Volume Fg, RAM Fg, Separator Fg, Tasks Fg.
colors_mono = ["FFFFFF", "2A2A2A", "2A2A2A", "2A2A2A", "9E9E9E", "2A2A2A"]

my_term = "termite"
my_browser = "min"

inner_gaps = 25
seps = " λ "

def init_keys():
    keys = [ 
        # Quit Session:
        Key([mod, "shift"], "l", lazy.spawn("kill -9 -1")),    
        # Run Launcher:
        Key([mod], "Return", lazy.spawn("rofi -show")),
           
        # Change Focus:R
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Right", lazy.layout.right()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Up", lazy.layout.up()),
        
        # Swap places:
        Key([mod, "shift"], "Left", lazy.layout.swap_left()),
        Key([mod, "shift"], "Right", lazy.layout.swap_right()),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
        Key([mod], "w", lazy.to_screen(0)),
        Key([mod], "y", lazy.to_screen(1)),
        Key([mod, "shift"], "w", lazy.window.to_screen(0)),
        Key([mod, "shift"], "y", lazy.window.to_screen(1)),
        
        # Resize keys:
        Key([mod], "i", lazy.layout.grow()),
        Key([mod], "m", lazy.layout.shrink()),
        Key([mod], "n", lazy.layout.normalize()),
        Key([mod], "o", lazy.layout.maximize()),
        # Move the master pane Left/Right:
        Key([mod, "shift"], "space", lazy.layout.flip()),
    
        # Change Layout:
        Key([mod], "Tab", lazy.next_layout()),
        # Close focused window:
        Key([mod], "q", lazy.window.kill()),
    
        # Restart qtile in place:
        Key([mod], "r", lazy.restart()),
    
        # Applications/Scripts Shortcuts:
        Key([mod], "t", lazy.spawn(my_term)),
        Key([mod], "b", lazy.spawn(my_browser)),
        Key([mod], "f", lazy.spawn("thunar")),
        Key([mod], "s", lazy.spawn("spotify")),
        
        # Volume control:
        Key([mod], "F7", lazy.spawn("amixer -c 0 -q set Master 1dB-")),
        Key([mod], "F8", lazy.spawn("amixer -c 0 -q set Master 1dB+")),
        ]
    return keys

keys = init_keys()

groups = [
    Group(
        "1",
        label="I"
    ),
    Group(
        "2",
        #matches=[Match(wm_class=["firefox"])],
        label="II"
    ),
    Group(
        "3",
        #matches=[Match(wm_class=["Emacs"])],
        label="III"
    ),
    Group(
        "4",
        #matches=[Match(wm_class=["libreoffice"])],
        label="IV"
    ),
    Group(
        "5",
        #matches=[Match(wm_class=["Thunderbird"])],
        label="V"
    ),
    Group(
        "6",
        #matches=[Match(wm_class=["code-oss"])],
        label="VI"
    ),
    Group(
        "7",
        label="VII"
    ),
    ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(
	border_normal = colors_mono[1],
	border_focus = colors_mono[0],
        border_width = 1,
        margin = inner_gaps,
    ),
]

widget_defaults = dict(
    font='Fira Code',
    fontsize=16,
    padding=4,
    background=colors_mono[0],
    margin_y = 100
)
extension_defaults = widget_defaults.copy()

def get_top_bar():
    return bar.Bar([
       widget.Spacer(bar.STRETCH),
       widget.Mpris2(
           foreground=colors_mono[3],
           name='spotify',
           objname="org.mpris.MediaPlayer2.spotify",
           display_metadata=['xesam:artist', 'xesam:title'],
           scroll_chars=None,
           stop_pause_text="",
       ),
       widget.TextBox(
           text=seps,
           foreground=colors_mono[4],
       ),
       widget.TextBox(
           text='Vol:',
           foreground=colors_mono[2],
       ),
       widget.Volume(
           foreground=colors_mono[2],
       ),
       widget.TextBox(
           text=seps,
           foreground=colors_mono[4],
       ),
       widget.Clock(
           format='%A, %B %d',
           foreground = colors_mono[1],
           mouse_callbacks = {"Button1": lambda: lazy.spawn("rofi -show")}
       ),
       widget.TextBox(
           text=seps,
           foreground=colors_mono[4],
       ),
       widget.Clock(
           format='%I:%M %p ',
           foreground = colors_mono[1],
           mouse_callbacks = {"Button1": lambda: lazy.spawn("rofi -show")}
       ),
    ], bar_size, background="FFFFFF")

screens = [
    Screen(top=get_top_bar()),
]
            
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    subprocess.call("/home/lominoss/.config/qtile/autostart.sh")
