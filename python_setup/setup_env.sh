#!/bin/bash
# Update system and install system dependencies
sudo pacman -Syu
sudo pacman -S python python-opencv gdal xorg-xwayland swayimg firefox

# Create and activate virtual environment
python -m venv yolox_env
source yolox_env/bin/activate.fish

# Install Python libraries in virtual environment
pip install torch torchvision easyocr numpy folium osmnx geopandas geopy matplotlib tensorboard

# Optional: Flask (uncomment if needed for API integration)
# pip install flask

# Verify installation
python -c "import cv2, torch, easyocr, folium, osmnx, geopandas, geopy, matplotlib, tensorboard; print('All good!')"

# Deactivate environment
deactivate
