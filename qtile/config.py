#  _                 _                     
# | | ___  _ __ ___ (_)_ __   ___  ___ ___ 
# | |/ _ \| '_ ` _ \| | '_ \ / _ \/ __/ __|
# | | (_) | | | | | | | | | | (_) \__ \__ \
# |_|\___/|_| |_| |_|_|_| |_|\___/|___/___/
#

# Imports:
from typing import List
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, EzKey, Match, Screen
from libqtile.lazy import lazy

# Preffered applications:
terminal = "termite"
browser = "min"
file_explorer = terminal + " -e ranger"
spotify = "spotify"

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
        "Super-<space>", lazy.layout.flip(), 
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
        "Super-t", lazy.spawn(terminal), 
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
        "Super-q", lazy.window.kill(), 
        desc = "Kill focused window"
    ),
    EzKey(
        "Super-r", lazy.restart(), 
        desc = "Restart Qtile"
    ),
    EzKey(
        "Super-Control-q", lazy.shutdown(), 
        desc = "Shutdown Qtile"
    ),
]

# Workspaces:
groups = [Group(i) for i in "123456789"]

# Workspaces keybindings:
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
    "margin": 20, 
    "border_width": 2,
    "single_border_width": 0,
    "border_normal": "#2E2E2E",
    "border_focus": "#FFFFFF",
    "new_client_position": "bottom",
    "change_size": 80,
    "change_ratio": .04
}

# Window layouts:
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
]

# Default bar settings:
widget_defaults = dict(
    font = "Fira Code",
    fontsize = 16,
    background = "#FFFFFF",
    foreground = "#2E2E2E",
    padding = 3,
)
extension_defaults = widget_defaults.copy()

# Bar widgets:
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(),
                # Spotify widget:
                widget.Mpris2(
                    name = 'spotify',
                    objname = "org.mpris.MediaPlayer2.spotify",
                    display_metadata = ['xesam:artist', 'xesam:title'],
                    scroll_chars = None,
                    stop_pause_text = None,
                    mouse_callbacks = {
                        "Button1": lambda: qtile.cmd_spawn("spotifycli --playpause"),
                        "Button4": lambda: qtile.cmd_spawn("spotifycli --next"),
                        "Button5": lambda: qtile.cmd_spawn("spotifycli --prev"),
                    }
                ),
                widget.TextBox(text="&lt;", foreground="#9E9E9E", padding=18),
                widget.Volume(fmt="Vol: {}"),
                widget.TextBox(text="&lt;", foreground="#9E9E9E", padding=18),
                widget.Clock(format='%A, %B %d'),
                widget.TextBox(text="&lt;", foreground="#9E9E9E", padding=18),
                widget.Clock(format='%I:%M:%S %p '),
            ],
            50, background = "#FFFFFF",
        ),
    ),
]

# Mouse controls:
mouse = [
    Drag(
        [mod], "Button1", lazy.window.set_position_floating(),
        start = lazy.window.get_position()
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(),
        start = lazy.window.get_size()
    ),
    Click(
        [mod], "Button2", lazy.window.bring_to_front()
    )
]

# Floating exceptions:
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
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
