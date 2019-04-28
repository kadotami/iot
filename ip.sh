#!/bin/sh
ipadd=""
while [ "$ipadd" = "" ]
do
  ipadd=`ip a show wlan0 | grep "inet " | cut -f6 -d ' ' | cut -f1 -d '/'`
  wait 1
done
python /home/pi/iot/ip.py ${ipadd}
