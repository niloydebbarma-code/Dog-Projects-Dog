import argparse

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='chosen model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', 
                        help='text file with dog names')
    return parser.parse_args()
