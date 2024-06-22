from classifier import classifier

def classify_images(images_dir, results_dic, model):
    results_dic.update({
        image_file: [details[0], classifier(images_dir + image_file, model).lower().strip(), 1 if details[0] in classifier(images_dir + image_file, model).lower().strip() else 0]
        for image_file, details in results_dic.items()
    })

# Example usage:
# classify_images('path/to/images/', results_dic, 'vgg')
