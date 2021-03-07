# source https://github.com/olivierverdier/zsh-git-prompt
source /Users/btf/Projects/etc/shell/mac/zsh-git-prompt/zshrc.sh

# style
PROMPT='%B%F{240}%2~%f%b $(git_super_status) '
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

# some ls aliases
alias ll='ls -alFG'
alias la='ls -A'
alias l='ls -CF'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/homebrew/Caskroom/miniforge/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.sh" ]; then
        . "/opt/homebrew/Caskroom/miniforge/base/etc/profile.d/conda.sh"
    else
        export PATH="/opt/homebrew/Caskroom/miniforge/base/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
