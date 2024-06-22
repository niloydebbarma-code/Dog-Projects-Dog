#!/bin/bash

# Define variables
dir="pet_images/"
arch=("resnet" "alexnet" "vgg")
dogfile="dognames.txt"
log_dir="logs"

# Create log directory if it doesn't exist
mkdir -p "$log_dir"

# Loop through each architecture and run check_images.py
for model in "${arch[@]}"
do
    python check_images.py --dir "$dir" --arch "$model" --dogfile "$dogfile" > "$log_dir/${model}_pet-images.txt" 2>&1
done
