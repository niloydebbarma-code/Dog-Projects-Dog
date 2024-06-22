def calculates_results_stats(results_dic):
    results_stats_dic = {
        'n_images': 0,
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'pct_match': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_notdogs': 0.0
    }
    
    for key in results_dic:
        pet_label, classifier_label, match, is_dog, classifier_is_dog = results_dic[key]
        
        results_stats_dic['n_images'] += 1
        
        if is_dog == 1:
            results_stats_dic['n_dogs_img'] += 1
            if classifier_is_dog == 1:
                results_stats_dic['n_correct_dogs'] += 1
                if match == 1:
                    results_stats_dic['n_correct_breed'] += 1
        else:
            results_stats_dic['n_notdogs_img'] += 1
            if classifier_is_dog == 0 and match == 0:
                results_stats_dic['n_correct_notdogs'] += 1
        
        if match == 1:
            results_stats_dic['n_match'] += 1
            
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
        
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    
    return results_stats_dic
