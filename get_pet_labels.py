def adjust_results4_isadog(results_dic, dogfile):
    # Read dog names from dogfile and store them in a set for fast lookup
    with open(dogfile, 'r') as file:
        dog_names = {line.strip() for line in file}

    # Iterate through results_dic and update each entry
    for key, (pet_label, classifier_label, match) in results_dic.items():
        # Determine if pet label and classifier label are dogs
        pet_is_dog = 1 if pet_label in dog_names else 0
        classifier_is_dog = 1 if classifier_label in dog_names else 0

        # Update results_dic with new values
        results_dic[key] = [pet_label, classifier_label, match, pet_is_dog, classifier_is_dog]
