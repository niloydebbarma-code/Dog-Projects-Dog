#!/bin/bash
python check_images.py --dir uploaded_images --arch resnet --dogfile dognames.txt
python check_images.py --dir uploaded_images --arch alexnet --dogfile dognames.txt
python check_images.py --dir uploaded_images --arch vgg --dog
