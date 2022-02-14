#!/bin/bash
case $1/$2 in
  pre/*)
    # Put here any commands expected to be run when suspending or hibernating.
    echo "Going to sleep" >> /tmp/sleeps-log.txt
    sh /etc/local.d/backlight.stop
    ;;
  post/*)
    # Put here any commands expected to be run when resuming from suspension or thawing from hibernation.
    echo "Waking up" >> /tmp/sleeps-log.txt
    sleep .1 && sh /etc/local.d/backlight.start
    ;;
esac
