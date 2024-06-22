def print_results(results_dic, results_stats, model, print_incorrect_dogs=False, print_incorrect_breed=False):
    print(f"Results for CNN Model Architecture {model}\n")
    print(f"N Images: {results_stats['n_images']}")
    print(f"N Dog Images: {results_stats['n_dogs_img']}")
    print(f"N Not-Dog Images: {results_stats['n_notdogs_img']}")
    print(f"Pct Match: {results_stats['pct_match']:.2f}%")
    print(f"Pct Correct Dogs: {results_stats['pct_correct_dogs']:.2f}%")
    print(f"Pct Correct Breed: {results_stats['pct_correct_breed']:.2f}%")
    print(f"Pct Correct Not-a-Dog: {results_stats['pct_correct_notdogs']:.2f}%")

    if print_incorrect_dogs:
        print("\nIncorrect Dog/Not Dog Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][1]}  Classifier: {results_dic[key][2]}")
    
    if print_incorrect_breed:
        print("\nIncorrect Dog Breed Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][3] == 1:
                print(f"Real: {results_dic[key][1]}  Classifier: {results_dic[key][2]}")
