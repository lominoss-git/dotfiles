#!/bin/bash

# options to be displayed
option0="Screen"
option1="Area"
option2="Window"

# options to be displyed
options="$option0\n$option1\n$option2"

selected="$(echo -e "$options" | rofi -dmenu -i -p "Screenshot")"
case $selected in
    $option0)
        cd ~/Pictures/Screenshots/ && sleep 1 && scrot;;
    $option1)
        cd ~/Pictures/Screenshots/ && scrot -s;;
    $option2)
        cd ~/Pictures/Screenshots/ && sleep 1 && scrot -u;;
esac
