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
from libqtile.config import Click, Drag, Group, EzKey, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from custom_max import CustomMax

# Color scheme:
colors = [
    # Bar colors:
    ["#E5E9F0", "#2E3440"], # Background
    ["#2E3440", "#E5E9F0"], # Time
    ["#2E3440", "#D8DEE9"], # Date
    ["#2E3440", "#E5E9F0"], # Battery
    ["#2E3440", "#D8DEE9"], # Volume
    ["#2E3440", "#E5E9F0"], # Memory
    ["#2E3440", "#D8DEE9"], # Spotify
    ["#2E3440", "#E5E9F0"], # Workspace
    # Window decorations:
    ["#D8DEE9", "#434C5E"], # Borders
]

# Window decorations:
border_width = 4
inner_gap = 12
outer_gap = 30
widget_padding = 18

# Preffered applications:
apps = {
    "terminal": "termite",
    "browser": "firefox",
    "file_explorer": "thunar",
    "editor": "termite -e micro",
    "music_player": "spotify"
}

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
    # Move windows:
    EzKey("Super-Shift-<Left>", lazy.layout.shuffle_left()), # Move left
    EzKey("Super-Shift-<Right>", lazy.layout.shuffle_right()), # Move right
    EzKey("Super-Shift-<Down>", lazy.layout.shuffle_down()), # Move down
    EzKey("Super-Shift-<Up>", lazy.layout.shuffle_up()), # Move Up
    EzKey("Super-Shift-f", lazy.layout.flip()), # Flip layout

    # Resize windows:
    EzKey("Super-<comma>", lazy.layout.grow()), # Grow window
    EzKey("Super-<period>", lazy.layout.shrink()), # Shrink window

    # Applications:
    KeyChord([mod], "a", [
        Key([], "b", lazy.spawn(apps["browser"])), # Launch browser
        Key([], "f", lazy.spawn(apps["file_explorer"])), # Launch file explorer
        Key([], "c", lazy.spawn(apps["editor"])), # Launch editor
        Key([], "s", lazy.spawn(apps["music_player"])) # Launch music player
    ]),
    EzKey("Super-<Return>", lazy.spawn(apps["terminal"])), # Launch terminal

    # Rofi scripts:
    KeyChord([mod], "space", [
        Key([], "a", lazy.spawn("rofi -show drun -display-drun Search")), # App menu
        Key([], "n", lazy.spawn("bash ./.config/rofi/scripts/rofi-wifi-menu.sh")), # Wi-Fi manu
        Key([], "p", lazy.spawn("rofi -show power-menu -modi power-menu:~/.config/rofi/scripts/rofi-power-menu")), # Power menu
        Key([], "s", lazy.spawn("bash ./.config/rofi/scripts/scrotmenu.sh")), # Screenshot menu
    ]),

    # Bar visibiliy:
    EzKey("Super-Shift-b", lazy.hide_show_bar()), # Hide bar

    # Volume controls:
    EzKey("Super-<F5>", lazy.spawn("amixer sset Master toggle")), # Toggle volume
    EzKey("Super-<F7>", lazy.spawn("amixer -c 0 -q set Master 1dB-")), # Volume down
    EzKey("Super-<F8>", lazy.spawn("amixer -c 0 -q set Master 1dB+")), # Volume up

    # Spotify controls:
    EzKey("Super-<F11>", lazy.spawn("spotifycli --playpause")), # Music toggle
    EzKey("Super-<F10>", lazy.spawn("spotifycli --prev")), # Music previous
    EzKey("Super-<F12>", lazy.spawn("spotifycli --next")), # Music next

    # Control Qtile:
    EzKey("Super-Control-<Tab>", lazy.next_layout()), # Switch layouts
    EzKey("Super-<Tab>", lazy.layout.next()), # Switch focus
    EzKey("Super-Shift-q", lazy.window.kill()), # Kill window
    EzKey("Super-r", lazy.restart()), # Restart qtile
]

# Workspaces:
groups = [Group(i) for i in "123456789"]

# Workspace keybindings:
for i in groups:
    keys.extend([
        # Switch to group:
        EzKey("Super-" + i.name, lazy.group[i.name].toscreen()),

        # Switch & move to group:
        EzKey("Super-Shift-" + i.name, lazy.window.togroup(i.name, switch_group=True)),
    ])

# Layout theme:
layout_theme = {
    "margin": inner_gap,
    "single_margin": inner_gap,
    "border_width": border_width,
    "single_border_width": border_width,
    "border_focus": colors[8][0],
    "border_normal": colors[8][1],
    "new_client_position": "bottom",
    "change_size": 80,
    "change_ratio": .04,
    "ratio": .4965,
}

# Tiling layouts:
layouts = [
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    CustomMax(
        # margin = inner_gap,
        border_width = border_width,
        border_focus = colors[8][0],
        border_normal = colors[8][1]
    ),
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
    border_focus = colors[8][0],
    border_normal = colors[8][1],
)

# Default bar settings:
widget_defaults = dict(
    font = "Fira Mono",
    fontsize = 16,
    padding = 0,
)
extension_defaults = widget_defaults.copy()

# Separator function:
def separate(foreground, background):
    return widget.TextBox(
        text = "\ue0ba",
        font = "Inconsolata for powerline",
        fontsize = 45,
        background = background,
        foreground = foreground
    )

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
                    foreground = colors[7][0],
                    background = colors[7][1],
                    margin_x = 18
                ),
                separate(colors[0][1], colors[7][1]),
                # Window name widget:
                widget.WindowName(
                    format = "{name}",
                    foreground = colors[0][0],
                    background = colors[0][1],
                    padding = 10
                ),
                separate(colors[6][1], colors[0][1]),
                # Spotify widget:
                widget.Mpris2(
                    name = "spotify",
                    objname = "org.mpris.MediaPlayer2.spotify",
                    display_metadata = ["xesam:artist", "xesam:title"],
                    max_chars = 35,
                    scroll_chars = 0,
                    stop_pause_text = None,
                    mouse_callbacks = {
                        "Button1": lambda: qtile.cmd_spawn("spotifycli --playpause"),
                        "Button4": lambda: qtile.cmd_spawn("spotifycli --next"),
                        "Button5": lambda: qtile.cmd_spawn("spotifycli --prev")
                    },
                    foreground = colors[6][0],
                    background = colors[6][1],
                    padding = widget_padding
                ),
                separate(colors[5][1], colors[6][1]),
                widget.Memory(
                    format = "MEM {MemPercent}%",
                    foreground = colors[5][0],
                    background = colors[5][1],
                    padding = widget_padding
                ),
                separate(colors[4][1], colors[5][1]),
                # Volume widget:
                widget.Volume(
                    fmt = "VOL {}",
                    foreground = colors[4][0],
                    background = colors[4][1],
                    padding = widget_padding
                ),
                separate(colors[3][1], colors[4][1]),
                # Battery widget:
                widget.TextBox(
                    text = "BAT 98.3%",
                    # format = "{percent:2.0%}",
                    # fmt = "BAT {}",
                    foreground = colors[3][0],
                    background = colors[3][1],
                    padding = widget_padding
                ),
                separate(colors[2][1], colors[3][1]),
                # Date widget:
                widget.Clock(
                    format = "%A, %B %d",
                    foreground = colors[2][0],
                    background = colors[2][1],
                    padding = widget_padding
                ),
                separate(colors[1][1], colors[2][1]),
                # Time widget:
                widget.Clock(
                    format = "%I:%M %p",
                    foreground = colors[1][0],
                    background = colors[1][1],
                    padding = widget_padding
                ),
            ], 48, background=colors[0], margin=[outer_gap - inner_gap, 0, 0, 0]
            # ], 48, background=colors[0], margin=[0, 0, 0, 0]
        ),
        left=bar.Gap(outer_gap - inner_gap),
        right=bar.Gap(outer_gap - inner_gap),
        top=bar.Gap(outer_gap - inner_gap),
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
bring_front_click = False
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
