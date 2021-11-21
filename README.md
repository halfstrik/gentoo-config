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
 * Set up screen locker
 * Set up Japanese and Russian inputs
 * Collect instruction for system maintenance
 * Set up emails in Emacs
 * Set up Conky
 * Update `slstatus` by chron and volume buttons (fewer updates, more accurate)
 * PyCharm does not remember GitHub token without Gnome keyring (https://youtrack.jetbrains.com/issue/PY-33817)
