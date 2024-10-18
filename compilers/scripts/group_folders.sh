#!/bin/bash

# Define the directory where your subfolders are located
BASE_DIR="../src"

# Iterate through each subfolder in the base directory
for dir in "$BASE_DIR"/*/; do
    # Get the first character of the directory name
    folder_name=$(basename "$dir")
    first_char="${folder_name:0:1}"

    # Create the destination parent directory based on the first character
    DEST_DIR="$BASE_DIR/$first_char"
    mkdir -p "$DEST_DIR"

    # Move the subfolder to the new parent directory
    mv "$dir" "$DEST_DIR"
done
