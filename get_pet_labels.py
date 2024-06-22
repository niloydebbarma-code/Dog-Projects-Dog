from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    
    for filename in listdir(image_dir):
        if not filename.startswith("."):
            pet_name = " ".join(filter(str.isalpha, filename.lower().split("_")))
            results_dic[filename] = [pet_name.strip()]
    
    return results_dic
