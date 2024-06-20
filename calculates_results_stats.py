def calculates_results_stats(results_dic):
    results_stats = dict()

    results_stats['n_dogs_img'] = 0
    results_stats['n_notdogs_img'] = 0
    results_stats['n_correct_dogs'] = 0
    results_stats['n_correct_notdogs'] = 0
    results_stats['n_correct_breed'] = 0
    results_stats['n_images'] = len(results_dic)

    for key in results_dic:
        if results_dic[key][3] == 1:
            results_stats['n_dogs_img'] += 1

            if results_dic[key][4] == 1:
                results_stats['n_correct_dogs'] += 1

            if results_dic[key][2] == 1:
                results_stats['n_correct_breed'] += 1
        else:
            results_stats['n_notdogs_img'] += 1

            if results_dic[key][4] == 0:
                results_stats['n_correct_notdogs'] += 1

    results_stats['pct_correct_dogs'] = (results_stats['n_correct_dogs'] / results_stats['n_dogs_img']) * 100.0
    results_stats['pct_correct_breed'] = (results_stats['n_correct_breed'] / results_stats['n_dogs_img']) * 100.0
    results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] / results_stats['n_notdogs_img']) * 100.0

    return results_stats
