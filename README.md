# Water Level Monitoring System

A Python-based solution for monitoring water levels in pipes using a Raspberry Pi and camera system. This project
captures video footage and can be used for real-time water level tracking.

## Project Outline

### Camera API
- The camera API will use libcamera (PiCamera2) and opencv to capture image/video from the camera and save it or pass it to the analysis module.

### Analysis Module
- The analysis module will use opencv to analyze the image/video and find the meniscus of the water level in the pipe. It will sample at a rate set by the user with the web server, calculate the flow rate, and save each day's minimum flow rate to be displayed by the web server.

### Web Server
- The web server will be a simple flask app that will have two primary functions: displaying daily data in various ways (possibly including graphs) and allowing the user to adjust the settings like sample rate and ROI (range of interest)

## Prerequisites

- Raspberry Pi (any model with camera support, I'm using a pi 5)
- Raspberry Pi compatible camera (This is the one I'm using https://www.amazon.com/MELIFE-Raspberry-Camera-Adjustable-Focus-Infrared/dp/B08RHZ5BJM)
- Python 3.x
- Raspberry Pi OS

## Installation

1. Clone this repository to your Raspberry Pi
2. Run the setup script. 