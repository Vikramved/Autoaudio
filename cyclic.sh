#!/bin/bash

# Navigate to the directory containing your main file

cd .

# Start the server on the desired port

python main.py &

# Wait for the server to start

sleep 5

# Run your bot script

python main.py

