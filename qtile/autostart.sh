#!/bin/bash

xrandr -s 1920x1080
nitrogen --restore &
compton --config ~/.config/compton/compton.conf &
