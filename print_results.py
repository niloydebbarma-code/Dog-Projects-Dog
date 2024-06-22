def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    print(f"\nModel: {model}\n")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dog Images: {results_stats_dic['n_notdogs_img']}\n")

    for key, value in results_stats_dic.items():
        if key.startswith('p'):
            print(f"{key}: {value}")

    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs:")
        for key, value in results_dic.items():
            if sum(value[3:]) == 1:
                print(f"Pet Image Label: {value[0]}  Classifier Label: {value[1]}")

    if print_incorrect_breed:
        print("\nIncorrectly Classified Breeds:")
        for key, value in results_dic.items():
            if sum(value[3:]) == 2 and not value[2]:
                print(f"Pet Image Label: {value[0]}  Classifier Label: {value[1]}")
