import os

def get_pet_labels(image_dir):
    results_dic = {}
    filename_list = os.listdir(image_dir)
    for filename in filename_list:
        if filename.startswith("."):
            continue
        pet_label = " ".join([word.lower() for word in filename.split("_")[:-1]])
        results_dic[filename] = [pet_label]
    return results_dic
