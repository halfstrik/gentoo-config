xbindkeys
./Programs/slstatus/slstatus &

# Fix Pycharm blank screen: https://unix.stackexchange.com/a/428908
export _JAVA_AWT_WM_NONREPARENTING=1

# Set walpaper
if [ -f ~/Pictures/Walpaper01.jpg ] ; then
    feh --bg-scale ~/Pictures/Walpaper01.jpg
fi

exec dbus-launch --sh-syntax --exit-with-session dwm
