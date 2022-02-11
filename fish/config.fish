
set fish_greeting
set PATH /home/lominoss/.flutter/flutter/bin $PATH

if set -q VIRTUAL_ENV
    echo -n
end

## PROMPT ##
function fish_prompt
    echo -e (pwd | sed "s=$HOME=~=g")
    echo -e '\033[1m>\033[0m '
end
## END OF PROMPT ##

## ALIASES ##
function update --wraps="sudo pacman -Syu" --wraps="sudo pacman -Syu ; yay -Syu' --wraps='echo\ -e\ \'\\033\[1mPacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1mAUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --wraps=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --description alias\ update=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu"
    echo -e '\033[33m\033[1m Pacman Update:\033[0m'
    sudo pacman -Syu
    echo -e '\033[32m\033[1m AUR Update:\033[0m'
    yay -Syu
end

function fetch --wraps=.config/fish/fm6000\ -w\ -c\ white\ -os\ \'Arch,\ btw!\'\ -de\ \'Qtile\'\ -sh\ \'Fish\' --description alias\ fetch=.config/fish/fm6000\ -w\ -c\ white\ -os\ \'Arch,\ btw!\'\ -de\ \'Qtile\'\ -sh\ \'Fish\'
  .config/fish/fm6000 -w -c white -os 'Arch, btw!' -de 'Qtile' -sh 'Fish' $argv;
end

function pdf --wraps='devour zathura' --description 'alias pdf=devour zathura'
    devour zathura $argv
end
## END OF ALIASES ##
