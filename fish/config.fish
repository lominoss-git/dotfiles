if status is-interactive
    # Commands to run in interactive sessions can go here
end

set fish_greeting
set PATH /home/lominoss/.flutter/flutter/bin $PATH

if set -q VIRTUAL_ENV
  echo -n
end

## PROMPT ##
function fish_prompt
  echo -e (pwd | sed "s=$HOME=~=g")
  echo -e '\033[1m→\033[0m '
end
## END OF PROMPT ##

## ALIASES ##
# function fetch --wraps=fm6000\ -c\ white\ -alice\ -n\ -o\ \'Arch,\ btw\' --wraps=fm6000\ -c\ white\ -phb\ -n\ -o\ \'Arch,\ btw\' --wraps=fm6000\ -c\ white\ -r\ -n\ -o\ \'Arch,\ btw\' --wraps=fm6000\ -c\ white\ -phb\ -n\ -de\ \'Qtile\'\ -s\ \'Fish\'\ -o\ \'Arch,\ btw\' --description alias\ fetch=fm6000\ -c\ white\ -phb\ -n\ -de\ \'Qtile\'\ -s\ \'Fish\'\ -o\ \'Arch,\ btw\'
#   fm6000 -c white -phb -n -de 'Qtile' -s 'Fish' -o 'Arch, btw'; 
# end

function pdf --wraps='devour zathura' --description 'alias pdf=devour zathura'
  devour zathura $argv; 
end

function update --wraps='sudo pacman -Syu' --wraps='sudo pacman -Syu ; yay -Syu' --wraps=echo\ -e\ \'\\033\[1mPacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1mAUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --wraps=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --description alias\ update=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu
  echo -e '\033[33m\033[1m→ Pacman Update:\033[0m' ; sudo pacman -Syu ; echo -e '\033[32m\033[1m→ AUR Update:\033[0m' ; yay -Syu; 
end

function c --wraps='clear'
  clear ; sh ~/.fetch;
end
## END OF ALIASES ##

# sh ~/.fetch
