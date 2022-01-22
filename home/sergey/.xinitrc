# TODO: iBus does not work anywhere except Emacs
# export XMODIFIERS=@im=ibus
# export GTK_IM_MODULE=ibus
# export QT_IM_MODULE=ibus
# ibus-daemon -drx

# Using xbindkeys instead
# setxkbmap -layout us,ru -option grp:win_space_toggle

xbindkeys
./Programs/slstatus/slstatus &
conky &

# Fix Pycharm blank screen: https://unix.stackexchange.com/a/428908
export _JAVA_AWT_WM_NONREPARENTING=1

# Set wallpaper
if [ -f ~/Pictures/Wallpaper01.jpg ] ; then
    feh --bg-scale ~/Pictures/Wallpaper01.jpg
fi

exec dbus-launch --sh-syntax --exit-with-session dwm
