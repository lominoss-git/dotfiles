# Qtile window manager configuration:
![VirtualBox_Arch Linux - Xmonad_25_09_2021_21_04_26](https://user-images.githubusercontent.com/79030093/134811916-469bb2ef-91e4-450f-9204-c6a924c2708d.png)

## Imports:
```python
# Imports:
from typing import List
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, EzKey, Match, Screen
from libqtile.lazy import lazy
```

## Variables:
```python
# Preffered applications:
terminal = "termite"
browser = "min"
file_explorer = terminal + " -e ranger"
spotify = "spotify"

mod = "mod4"
```
