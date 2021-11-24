#  _                 _ 
# | | ___  _ __ ___ (_)
# | |/ _ \| '_ ` _ \| |
# | | (_) | | | | | | |
# |_|\___/|_| |_| |_|_|
#  _ __   ___  ___ ___ 
# | '_ \ / _ \/ __/ __|
# | | | | (_) \__ \__ \
# |_| |_|\___/|___/___/
#

# Imports:
import os
import subprocess
from typing import List
from libqtile import qtile, extension
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, EzKey, Match, Screen
from libqtile.lazy import lazy

# Color scheme:
colors = [
    # Bar colors:
    "#2E3440", # 0. Background.
    "#2E3440", # 1. Arch widget foreground.
    "#E5E9F0", # 2. Arch widget background.
    "#2E3440", # 3. Time widget foreground.
    "#D8DEE9", # 4. Time widget background.
    "#2E3440", # 5. Date widget foreground.
    "#E5E9F0", # 6. Date widget background.
    "#2E3440", # 7. Volume widget foreground.
    "#D8DEE9", # 8. Volume widget background.
    "#2E3440", # 9. Pomodoro widget foreground.
    "#E5E9F0", # 10. Pomodoro widget background.
    "#2E3440", # 11. Spotify widget foreground.
    "#D8DEE9", # 12. Spotify widget background.
    "#2E3440", # 13. Current workspace foreground.
    "#D8DEE9", # 14. Current workspace background.

    # Window decorations:
    "#D8DEE9", # 15. Active window's border.
    "#4C566A", # 16. Inactive window's border.
]

# Window decorations:
border_width = 4
window_gap = 20

# Preffered applications:
terminal = "termite"
browser = "firefox"
file_explorer = "thunar"
spotify = "spotify"
editor = "code"

mod = "mod4"

# Keybinding modifiers:
EzKey.modifier_keys = {
    "Super": "mod4",
    "Alt": "mod1",
    "Shift": "shift",
    "Control": "control"
}

# Keybindings:
keys = [
    # Switch focus:
    EzKey(
        "Super-<Tab>", lazy.layout.next(),
        desc = "Move window focus to the next window"
    ),
    EzKey(
        "Super-Shift-<Tab>", lazy.layout.previous(),
        desc = "Move window focus to the previous window"
    ),

    # Move windows:
    EzKey(
        "Super-Shift-<Left>", lazy.layout.shuffle_left(),
        desc = "Move window to the left"
    ),
    EzKey(
       "Super-Shift-<Right>", lazy.layout.shuffle_right(),
        desc = "Move window to the right"
    ),
    EzKey(
        "Super-Shift-<Down>", lazy.layout.shuffle_down(),
        desc = "Move window down"
    ),
    EzKey(
        "Super-Shift-<Up>", lazy.layout.shuffle_up(), 
        desc = "Move window up"
    ),
    EzKey(
        "Super-Shift-f", lazy.layout.flip(), 
        desc = "Flip window stacks"
    ),

    # Resize windows:
    EzKey(
        "Super-<comma>", lazy.layout.grow(),
        desc = "Grow window"
    ),
    EzKey(
        "Super-<period>", lazy.layout.shrink(),
        desc = "Shrink window"
    ),
    EzKey(
        "Super-n", lazy.layout.normalize(),
        desc = "Reset all window sizes"
    ),

    # Launch applications:
    EzKey(
        "Super-<space>", lazy.spawn("rofi -show drun -display-drun Search"),
        desc = "Launch launcher"
    ),
    EzKey(
        "Super-<Return>", lazy.spawn(terminal),
        desc = "Launch terminal"
    ),
    EzKey(
        "Super-b", lazy.spawn(browser),
        desc = "Launch browser"
    ),
    EzKey(
        "Super-f", lazy.spawn(file_explorer),
        desc = "Launch file explorer"
    ),
    EzKey(
        "Super-s", lazy.spawn(spotify),
        desc = "Launch Spotify"
    ),
    EzKey(
        "Super-c", lazy.spawn(editor),
        desc = "Launch code editor"
    ),
    
    # Bar visibiliy:
    EzKey(
        "Super-Shift-b", lazy.hide_show_bar(position="bottom"),
        desc = "Toggle bar visibility"
    ),
    
    # Volume controls:
    EzKey(
        "Super-<F5>", lazy.spawn("amixer sset Master toggle"),
        desc = "Toggle mute"
    ),
    EzKey(
        "Super-<F7>", lazy.spawn("amixer -c 0 -q set Master 1dB-"),
        desc = "Lower volume"
    ),
    EzKey(
        "Super-<F8>", lazy.spawn("amixer -c 0 -q set Master 1dB+"),
        desc = "Raise volume"
    ),

    # Spotify controls:
    EzKey(
        "Super-<F11>", lazy.spawn("spotifycli --playpause"),
        desc = "Toggle pause"
    ),
    EzKey(
        "Super-<F10>", lazy.spawn("spotifycli --prev"),
        desc = "Play previous track"
    ),
    EzKey(
        "Super-<F12>", lazy.spawn("spotifycli --next"),
        desc = "Play next track"
    ),

    # Control Qtile:
    EzKey(
        "Super-Control-<Tab>", lazy.next_layout(),
        desc = "Switch layouts"
    ),
    EzKey(
        "Super-Shift-q", lazy.window.kill(),
        desc = "Kill focused window"
    ),
    EzKey(
        "Super-r", lazy.restart(),
        desc = "Restart Qtile"
    ),
    EzKey(
        "Super-Shift-l", lazy.shutdown(),
        desc = "Shutdown Qtile"
    ),
]

# Workspaces:
groups = [Group(i) for i in "123456789"]

# Workspace keybindings:
for i in groups:
    keys.extend([
        # Switch to group:
        EzKey(
            "Super-" + i.name, lazy.group[i.name].toscreen(),
            desc = "Switch to group {}".format(i.name)
        ),

        # Switch & move to group:
        EzKey(
            "Super-Shift-" + i.name, lazy.window.togroup(i.name, switch_group=True),
            desc = "Switch to & move focused window to group {}".format(i.name)
        ),
    ])

# Layout theme:
layout_theme = {
    "margin": window_gap,
    "single_margin": window_gap,
    "border_width": border_width,
    "single_border_width": border_width,
    "border_focus": colors[15],
    "border_normal": colors[16],
    "new_client_position": "bottom",
    "change_size": 80,
    "change_ratio": .04,
    "ratio": .4965,
}

# Tiling layouts:
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width = border_width,
    border_focus = colors[15],
    border_normal = colors[16],
)

# Default bar settings:
widget_defaults = dict(
    font = "Fira Mono",
    fontsize = 16,
    padding = 0,
)
extension_defaults = widget_defaults.copy()

# Bar widgets:
screens = [
    Screen(
        bottom = bar.Bar(
            [
                # Current group widget:
                widget.AGroupBox(
                    borderwidth = 0,
                    mouse_callbacks = {
                        "Button1": lambda: qtile.cmd_spawn("rofi -show drun -display-drun Search"),
                        "Button4": lambda: qtile.current_screen.cmd_next_group(),
                        "Button5": lambda: qtile.current_screen.cmd_prev_group()
                    },
                    foreground = colors[11],
                    background = colors[12],
                    margin_x = 14
                ),
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[0],
                    background = colors[12]
                ),
                widget.Spacer(),
                # Spotify widget:
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[12],
                    background = colors[0]
                ),
                widget.Mpris2(
                    name = "spotify",
                    objname = "org.mpris.MediaPlayer2.spotify",
                    display_metadata = ["xesam:artist", "xesam:title"],
                    scroll_chars = None,
                    stop_pause_text = None,
                    mouse_callbacks = {
                        "Button1": lambda: qtile.cmd_spawn("spotifycli --playpause"),
                        "Button4": lambda: qtile.cmd_spawn("spotifycli --next"),
                        "Button5": lambda: qtile.cmd_spawn("spotifycli --prev")
                    },
                    foreground = colors[11],
                    background = colors[12],
                    padding = 15
                ),
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[10],
                    background = colors[12]
                ),
                # Pomodoro widget:
                widget.Pomodoro(
                    prefix_break = "Break: ",
                    prefix_long_break = "Long break: ",
                    prefix_paused = "Paused",
                    prefix_inactive = "Pomodoro",
                    color_active = colors[9],
                    color_break = colors[9],
                    color_inactive = colors[9],
                    foreground = colors[9],
                    background = colors[10],
                    padding = 15
                ),
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[8],
                    background = colors[10]
                ),
                # Volume widget:
                widget.Volume(
                    fmt = "Vol: {}", 
                    foreground = colors[7], 
                    background = colors[8],
                    padding = 15
                ),
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[6],
                    background = colors[8]
                ),
                # Date widget:
                widget.Clock(
                    format = "%A, %B %d", 
                    foreground = colors[5], 
                    background = colors[6],
                    padding = 15
                ), 
                widget.TextBox(
                    text = "\ue0be", 
                    font = "Inconsolata for powerline", 
                    fontsize = 45,
                    foreground = colors[4],
                    background = colors[6],
                ),
                # Time widget:
                widget.Clock(
                    format = "%I:%M:%S %p", 
                    foreground = colors[3], 
                    background = colors[4],
                    padding = 15
                ),
            ], 45, background=colors[0], margin=[0, 0, 0, 0]
        ),
    ),
]

# Mouse controls:
mouse = [
    Click(
        [mod], "Button1", lazy.window.bring_to_front()
    ),
    Click(
        [mod, "shift"], "Button2", lazy.window.toggle_floating()
    ),
    Drag(
        [mod, "shift"], "Button1", lazy.window.set_position_floating(),
        start = lazy.window.get_position()
    ),
    Drag(
        [mod, "shift"], "Button3", lazy.window.set_size_floating(),
        start = lazy.window.get_size()
    )
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Startup commands:
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# Java UI toolkits:
wmname = "LG3D"
