#!/bin/bash

# Check if Homebrew is installed, install if not
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Update Homebrew
brew update

# Install Google Chrome
if ! command -v google-chrome &> /dev/null; then
    echo "Google Chrome not found. Installing Google Chrome..."
    brew install --cask google-chrome
else
    echo "Google Chrome already installed. Skipping..."
fi

# Install Chromedriver
if ! command -v chromedriver &> /dev/null; then
    echo "Chromedriver not found. Installing Chromedriver..."
    brew install chromedriver
else
    echo "Chromedriver already installed. Skipping..."
fi

echo "Installation complete!"