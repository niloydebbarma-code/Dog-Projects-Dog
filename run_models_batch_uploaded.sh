#!/bin/sh

# Function to run check_images.py with specified architecture and output file
run_model() {
    python check_images.py --dir uploaded_images/ --arch $1 --dogfile dognames.txt > $2
}

# Use case statement to determine which model to run
case $1 in
    resnet)
        run_model "resnet" "resnet_uploaded-images.txt"
        ;;
    alexnet)
        run_model "alexnet" "alexnet_uploaded-images.txt"
        ;;
    vgg)
        run_model "vgg" "vgg_uploaded-images.txt"
        ;;
    *)
        echo "Invalid model specified. Usage: $0 {resnet|alexnet|vgg}"
        exit 1
        ;;
esac
