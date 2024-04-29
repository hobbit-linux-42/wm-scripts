#!/usr/bin/bash
cd /sys/class/leds
while true
sleep 1
do
	state=$(cat /home/gian42/.config/rgbkeyboard.state)
	for i in *scroll*
	do
		if [ $(cat $i/brightness) != $state ]
		then
			echo $state > $i/brightness
		fi
	done
done
