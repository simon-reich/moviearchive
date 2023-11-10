#!/bin/sh

# Navigate to the backend directory
cd ~/git/private/moviearchive/app/backend || { echo "Failed to cd to backend"; exit 1; }

# Start docker-compose
gnome-terminal -- sh -c "docker-compose up"

# Add a sleep command to give Docker some time to start
sleep 10

# Navigate to the app/src directory
cd ./app/src || { echo "Failed to cd to app/src"; exit 1; }

# Run flask command
gnome-terminal -- sh -c "pipenv run flask run --debug"

# Navigate to the frontend directory
cd ~/git/private/moviearchive/app/frontend || { echo "Failed to cd to frontend"; exit 1; }

# Start npm
gnome-terminal -- sh -c "npm run dev"
