#!/bin/bash
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install it first."
    exit 1
fi
echo "Installing OpenClaw..."
sudo npm install -g openclaw
echo "Starting OpenClaw Onboarding..."
openclaw onboard
