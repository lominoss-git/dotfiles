set fish_greeting

set MICRO_TRUECOLOR 1

## PROMPT ##
function fish_prompt
    set -l last_status $status
    set -l cwd (prompt_pwd)
    set -l duration (math $CMD_DURATION/1000)

    if not test $last_status -eq 0
        set_color --bold white -b red
        echo -n ' '$last_status' '
        set_color normal
    end

    # Display current path
    set_color --bold 2E3440 -b ECEFF4
    echo -n "  $cwd "

    if set -q VIRTUAL_ENV
        echo -n -s (set_color --bold white -b 5E81AC) "  " (basename "$VIRTUAL_ENV") " " (set_color normal)
    end

    # Show git branch and dirty state
    set -l git_branch (command git symbolic-ref HEAD 2> /dev/null | sed -e 's|^refs/heads/||')
    set -l git_dirty (command git status -s --ignore-submodules=dirty 2> /dev/null)
    if test -n "$git_branch"
        if test -n "$git_dirty"
            set_color --bold 2E3440 -b yellow
            echo -n "  $git_branch "
        else
            set_color --bold 2E3440 -b green
            echo -n "  $git_branch "
        end
    end

    if not test $CMD_DURATION = "0"
        set_color --bold white -b 4c566a
        echo -n ' '$duration's '
        set_color normal
    end

    # Add a space
    set_color normal
    echo -n ' '
end
## END OF PROMPT ##

## ALIASES ##
function update --wraps="sudo pacman -Syu" --wraps="sudo pacman -Syu ; yay -Syu' --wraps='echo\ -e\ \'\\033\[1mPacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1mAUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --wraps=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu --description alias\ update=echo\ -e\ \'\\033\[1m-\ Pacman\ Update\\033\[0m:\'\ \;\ sudo\ pacman\ -Syu\ \;\ echo\ -e\ \'\\033\[1m-\ AUR\ Update\\033\[0m:\'\ \;\ yay\ -Syu"
    echo -e '\033[33m\033[1mPacman Update:\033[0m'
    sudo pacman -Syu
    echo -e '\033[32m\033[1mAUR Update:\033[0m'
    yay -Syu
end

function fetch --wraps=.config/fish/fm6000\ -w\ -c\ white\ -os\ \'Arch,\ btw!\'\ -de\ \'Qtile\'\ -sh\ \'Fish\' --description alias\ fetch=.config/fish/fm6000\ -w\ -c\ white\ -os\ \'Arch,\ btw!\'\ -de\ \'Qtile\'\ -sh\ \'Fish\'
  ~/.config/fish/fm6000 -w -c white -os 'Arch, btw!' -de 'Qtile' -sh 'Fish' $argv;
end

function pdf --wraps='devour zathura' --description 'alias pdf=devour zathura'
    devour zathura $argv
end
## END OF ALIASES ##
