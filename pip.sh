#!/bin/bash

# pip.sh

echo "Installing dependencies..."

# Upgrade pip
python3 -m pip install --upgrade pip

# Install from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping..."
fi

echo "Setup complete."
