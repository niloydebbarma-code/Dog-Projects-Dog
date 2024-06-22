def adjust_results4_isadog(results_dic, dogfile):
    dognames = set()
    with open(dogfile, "r") as f:
        for line in f:
            dognames.add(line.strip())
    
    for key in results_dic:
        is_dog = 1 if results_dic[key][0] in dognames else 0
        classifier_is_dog = 1 if results_dic[key][1] in dognames else 0
        results_dic[key].extend([is_dog, classifier_is_dog])
