from os import listdir

def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    results_dic = dict()

    for filename in filename_list:
        if filename[0] != ".":
            pet_label = " ".join([word.lower() for word in filename.split('_') if word.isalpha()])
            results_dic[filename] = [pet_label]

    return results_dic
