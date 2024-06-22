def calculates_results_stats(results_dic):
    stats = {
        'n_images': len(results_dic),
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'pct_match': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_notdogs': 0.0
    }
    
    for key in results_dic:
        if results_dic[key][3] == 1:
            stats['n_dogs_img'] += 1
        else:
            stats['n_notdogs_img'] += 1
        
        if results_dic[key][2] == 1:
            stats['pct_match'] += 1
        
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            stats['pct_correct_dogs'] += 1
        
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            stats['pct_correct_breed'] += 1
        
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            stats['pct_correct_notdogs'] += 1
    
    stats['pct_match'] = (stats['pct_match'] / stats['n_images']) * 100.0
    stats['pct_correct_dogs'] = (stats['pct_correct_dogs'] / stats['n_dogs_img']) * 100.0
    stats['pct_correct_breed'] = (stats['pct_correct_breed'] / stats['n_dogs_img']) * 100.0
    stats['pct_correct_notdogs'] = (stats['pct_correct_notdogs'] / stats['n_notdogs_img']) * 100.0
    
    return stats
