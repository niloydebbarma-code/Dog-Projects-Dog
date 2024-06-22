def check_command_line_arguments(in_arg):
    if in_arg:
        print(f"Command Line Arguments:\n     dir = {in_arg.dir}\n    arch = {in_arg.arch}\n dogfile = {in_arg.dogfile}")
    else:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")

def check_creating_pet_image_labels(results_dic):
    if results_dic:
        print(f"\nPet Image Label Dictionary has {len(results_dic)} key-value pairs.")
        print(f"Below are {min(len(results_dic), 10)} of them:")

        for i, (key, value) in enumerate(results_dic.items()):
            if i < 10:
                print(f"{i+1:2d} key: {key:>30}  label: {value[0]:>26}")
    else:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")

def check_classifying_images(results_dic):
    if results_dic:
        n_match = sum(1 for key, value in results_dic.items() if value[2] == 1)
        n_notmatch = sum(1 for key, value in results_dic.items() if value[2] == 0)

        print("\n     MATCH:")
        for key, value in results_dic.items():
            if value[2] == 1:
                print(f"\n{key:>30}: \nReal: {value[0]:>26}   Classifier: {value[1]:>30}")

        print("\n NOT A MATCH:")
        for key, value in results_dic.items():
            if value[2] == 0:
                print(f"\n{key:>30}: \nReal: {value[0]:>26}   Classifier: {value[1]:>30}")

        print(f"\n# Total Images {len(results_dic)} # Matches: {n_match} # NOT Matches: {n_notmatch}")
    else:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")

def check_classifying_labels_as_dogs(results_dic):
    if results_dic:
        n_match = sum(1 for key, value in results_dic.items() if value[2] == 1)
        n_notmatch = sum(1 for key, value in results_dic.items() if value[2] == 0)

        print("\n     MATCH:")
        for key, value in results_dic.items():
            if value[2] == 1:
                print(f"\n{key:>30}: \nReal: {value[0]:>26}   Classifier: {value[1]:>30}  \nPetLabelDog: {value[3]:1d}  ClassLabelDog: {value[4]:1d}")

        print("\n NOT A MATCH:")
        for key, value in results_dic.items():
            if value[2] == 0:
                print(f"\n{key:>30}: \nReal: {value[0]:>26}   Classifier: {value[1]:>30}  \nPetLabelDog: {value[3]:1d}  ClassLabelDog: {value[4]:1d}")

        print(f"\n# Total Images {len(results_dic)} # Matches: {n_match} # NOT Matches: {n_notmatch}")
    else:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")

def check_calculating_results(results_dic, results_stats_dic):
    if results_stats_dic:
        n_images = len(results_dic)
        n_pet_dog = sum(1 for key, value in results_dic.items() if value[3] == 1)
        n_pet_notd = n_images - n_pet_dog
        n_class_cdog = sum(1 for key, value in results_dic.items() if value[4] == 1 and value[3] == 1)
        n_class_cnotd = sum(1 for key, value in results_dic.items() if value[4] == 0 and value[3] == 0)
        n_match_breed = sum(1 for key, value in results_dic.items() if value[2] == 1 and value[3] == 1 and value[4] == 1)
        pct_corr_dog = (n_class_cdog / n_pet_dog) * 100 if n_pet_dog > 0 else 0
        pct_corr_notdog = (n_class_cnotd / n_pet_notd) * 100 if n_pet_notd > 0 else 0
        pct_corr_breed = (n_match_breed / n_pet_dog) * 100 if n_pet_dog > 0 else 0

        print(f"\n ** Statistics from calculates_results_stats() function:")
        print(f"N Images: {results_stats_dic['n_images']}  N Dog Images: {results_stats_dic['n_dogs_img']}  N NotDog Images: {results_stats_dic['n_notdogs_img']}")
        print(f"Pct Corr dog: {results_stats_dic['pct_correct_dogs']:5.1f} Pct Corr NOTdog: {results_stats_dic['pct_correct_notdogs']:5.1f}  Pct Corr Breed: {results_stats_dic['pct_correct_breed']:5.1f}")
        print("\n ** Check Statistics - calculated from this function as a check:")
        print(f"N Images: {n_images}  N Dog Images: {n_pet_dog}  N NotDog Images: {n_pet_notd}")
        print(f"Pct Corr dog: {pct_corr_dog:5.1f} Pct Corr NOTdog: {pct_corr_notdog:5.1f}  Pct Corr Breed: {pct_corr_breed:5.1f}")
    else:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
