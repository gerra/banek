#!/bin/bash

log_file="logs.txt"
script_name=$(basename "$0")

# Generate a random hour between 15 (3:00 PM) and 20 (8:00 PM)
random_hour=$((RANDOM % 6 + 15))
# Generate a random minute between 0 and 59
random_minute=$((RANDOM % 60))
# Construct the time string in HH:MM format
scheduled_time=$(printf "%02d:%02d" "$random_hour" "$random_minute")

command_to_run="python3 $HOME/Projects/banek/send_anek.py"

echo "$command_to_run" | at "$scheduled_time"

echo "[$script_name] $(date '+%Y-%m-%d %H:%M:%S') - Scheduled at $scheduled_time: $command_to_run" >> "$log_file"