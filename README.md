# gentoo-config
Here is my Gentoo GNU/Linux config for MacBook Air 2012,
created mostly for educational purposes and to help keep track of my setup.

## Sync files
```shell
su -  # (if sync git -> root)
cd /home/sergey/Projects/gentoo-config/
python syncfiles.py
```

## TODOs
 * Wireless card uses open-source driver which may cause problems.
 * Screen brightness goes to max after lid re-open.
 * ~~Set up screen locker~~ (slock, find out why laptop not sleep on lid close)
 * Set up Japanese ~~and Russian~~ inputs (partially - Japanese only in Emacs with mozc-mode, re-try iBus)
 * Collect instruction for system maintenance
 * Set up emails in Emacs
 * ~~Set up Conky~~
 * ~~Update `slstatus` by chron and volume buttons (fewer updates, more accurate)~~
 * PyCharm does not remember GitHub token without Gnome keyring (https://youtrack.jetbrains.com/issue/PY-33817)
 * Setup bluetooth headset (work in progress, making bluez-alsa work, no PulseAudio for now)

## Useful links
https://wiki.archlinux.org/title/Mac

## Wireless download problem
Problem appears with `wget`, to reproduce:
```wget https://download.jetbrains.com/python/pycharm-community-2021.2.3.tar.gz```

One of the ways to fix - limit bandwidth (https://unix.stackexchange.com/a/28203):
```tc qdisc add dev wlp2s0b1 root tbf rate 128kbit latency 50ms burst 1540```
To undo:
```tc qdisc del dev wlp2s0b1 root```

## Sound in bluetooth headset
Works in Chrome with
```google-chrome-stable --alsa-output-device=bluealsa```
No additional configs used

Make TOZO-T10 default (all apps need restart)
```ln -s .asoundrc_tozo_t10 .asoundrc```
Remove default
```rm .asoundrc```
