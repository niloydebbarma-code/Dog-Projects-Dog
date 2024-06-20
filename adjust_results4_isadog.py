def adjust_results4_isadog(results_dic, dogfile):
    dognames = dict()
    
    with open(dogfile) as f:
        line = f.readline()
        while line != "":
            line = line.rstrip()
            if line not in dognames:
                dognames[line] = 1
            line = f.readline()
    
    for key in results_dic:
        if results_dic[key][0] in dognames:
            if results_dic[key][1] in dognames:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        else:
            if results_dic[key][1] in dognames:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))
