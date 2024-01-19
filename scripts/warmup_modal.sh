#!/bin/bash

lock_file="/tmp/ml_warmup.lock"
timezone=${TZ:-"GMT-3"}

if [ -e "$lock_file" ]; then
    echo "Script is already running. Exiting."
    exit 1
fi

# Load environment variables from .env file
if [ -f .env ]; then
    source .env
else
    echo ".env file not found. Make sure it exists in the same directory as the script. Using default values."
fi

trap "rm -f $lock_file" EXIT # Remove the lock file on script exit

touch "$lock_file"

while true; do
    current_hour=$(TZ="$timezone" date +%H)

    if ((current_hour >= 9 && current_hour < 17)); then
        echo "Executing command..."
        curl -s $EMBEDDING_API_ENDPOINT_SINGLE
        break # Break out of the loop after executing the command once during business hours
    else
        echo "Outside of business hours. Checking again in 10 minutes..."
        sleep 600 # Wait for 10 minutes before checking again
    fi
done
