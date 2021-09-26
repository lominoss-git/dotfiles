# Qtile window manager configuration
![VirtualBox_Arch Linux - Xmonad_25_09_2021_21_04_26](https://user-images.githubusercontent.com/79030093/134811916-469bb2ef-91e4-450f-9204-c6a924c2708d.png)
## Imports
```python
# Imports:
from typing import List
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, EzKey, Match, Screen
from libqtile.lazy import lazy
```
## Variables
```python
# Preffered applications:
terminal = "termite"
browser = "min"
file_explorer = terminal + " -e ranger"
spotify = "spotify"

mod = "mod4"
```
## Keybindings
### Switch focus
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + TAB  | Move window focus to the next window  |
| SUPER+ SHIFT + TAB  | Move window focus to the previous window  |
### Move windows
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + SHIFT + LEFT  | Move window to the left  |
| SUPER + SHIFT + RIGHT  | Move window to the right  |
| SUPER + SHIFT + DOWN  | Move window down  |
| SUPER + SHIFT UP  | Move window up  |
| SUPER + SPACE  | Flip window stacks  |
### Resize windows
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + COMMA  | Grow window  |
| SUPER + PERIOD  | Shrink window  |
| SUPER + N  | Reset all window sizes  |
### Launch applications
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + T  | Launch terminal  |
| SUPER + B  | Launch browser  |
| SUPER + F  | Launch file explorer  |
| SUPER + S  | Launch Spotify  |
### Volume controls
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + F5  | Toggle mute  |
| SUPER + F7  | Lower volume  |
| SUPER + F8  | Raise volume  |
### Spotify controls
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + F11  | Toggle pause  |
| SUPER + F10  | Play previous track  |
| SUPER + F12  | Play next track  |
### Control Qtile
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + CONTROL + TAB  | Switch layouts  |
| SUPER + Q  | Kill focused window  |
| SUPER + R  | Restart Qtile  |
| SUPER + CONTROL + Q  | Shutdown Qtile  |
### Workspaces
| Keybinding  | Action |
| ------------- | ------------- |
| SUPER + 1-9  | Move focus to workspace  |
| SUPER + SHIFT + 1-9  | Move focused window to workspace  |

```python
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
        desc = "Launch music player"
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
        desc = "Toggle between layouts"
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
```
## Layouts
### Layout theme
```python
# Layout theme:
layout_theme = {
    "margin": 20, 
    "border_width": 1,
    "single_border_width": 0,
    "border_normal": "#2E2E2E",
    "border_focus": "#FFFFFF",
    "new_client_position": "bottom",
    "change_size": 80,
    "change_ratio": .04
}
```
### Layouts
```python
# Window layouts:
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(),
]
```
