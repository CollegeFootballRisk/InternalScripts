#!/bin/bash
#bot.sh
process=bot.py
makerun="/usr/bin/python3 /srv/random_internal_scripts/discord_bot/bot.py"

if ps ax | grep -v grep | grep $process > /dev/null
then
    exit
else
    $makerun > /var/log/discord_bot.log &
fi

exit