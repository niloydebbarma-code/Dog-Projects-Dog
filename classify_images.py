from classifier import classifier

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        model_label = classifier(images_dir + key, model).lower().strip()
        results_dic[key].extend([model_label, 1 if model_label in results_dic[key][0] else 0])
