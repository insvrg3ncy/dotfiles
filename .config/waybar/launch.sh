#!/usr/bin/env sh
killall waybar

theme="/Oxocarbon-Vertical"

if [ -f ~/.cache/.themestyle.sh ]; then
    saved_theme=$(cat ~/.cache/.themestyle.sh)
    # Проверяем, есть ли разделитель
    if [[ "$saved_theme" == *";"* ]]; then
        # Если есть — берём первую часть (название темы)
        theme=$(echo "$saved_theme" | cut -d';' -f1)
    else
        # Если нет — используем как есть
        theme="$saved_theme"
    fi
fi

if [ ! -d ~/.config/waybar/themes$theme ]; then
    theme="/CatMocha-HSlim"
fi

if [[ $USER = "main" ]]; then
    waybar -c ~/.config/waybar/themes$theme/myconfig -s ~/.config/waybar/themes$theme/style.css &
else
    waybar -c ~/.config/waybar/themes$theme/config -s ~/.config/waybar/themes$theme/style.css &
fi
