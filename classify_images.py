import argparse

def get_input_args():
    parser = argparse.ArgumentParser(description='Classify pet images using a CNN model.')
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', choices=['resnet', 'alexnet', 'vgg'], help='CNN model architecture (choices: resnet, alexnet, vgg)')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='Text file with dog names')
    args = parser.parse_args()
    return args
