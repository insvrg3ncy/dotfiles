# haii!! there are my dotfiles

## deps

```
sudo pacman -S btop caja fish gtk3 gtk4 hyprland kitty systemd waybar hyprpicker hyprcursor hyprshot awww cava swaync swayimg
```

## install

```
git clone https://github.com/insvrg3ncy/dotfiles ~/.dotfiles
cd ~/.dotfiles
stow -v -t ~ .
```

## structure

```
btop/     - system monitor
caja/     - file manager
fish/     - shell
gtk-3.0/  - gtk3 configs
gtk-4.0/  - gtk4 configs
hypr/     - hyprland wm
kitty/    - terminal
systemd/  - user services
waybar/   - status bar
```

## stack

- hyprland - tiling wm with animations
- waybar - status bar
- kitty - terminal
- fish - shell with autocomplete
- btop - resource monitor
- cava - audio visualizer

## post-install

```
chsh -s /usr/bin/fish
```

logout & back in
