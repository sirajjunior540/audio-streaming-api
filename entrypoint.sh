#!/bin/bash
# Entrypoint script for setting up the server

# Update package list and install portaudio19-dev
sudo apt-get update
sudo apt-get install -y portaudio19-dev

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000
