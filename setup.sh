#!/bin/bash

if [ -f /proc/device-tree/model ] && grep -q -i "raspberry pi" /proc/device-tree/model; then
    sudo apt-get install libcamera-apps python3-picamera2 python3-opencv -y
else
    echo "This is not a Raspberry Pi. This project is only compatible with Raspberry Pi OS"
fi