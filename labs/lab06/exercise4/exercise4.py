def synchronize_databases(legacy_list, modern_set, blacklist):
    legacy_set = set(legacy_list)
    clean_legacy_set = set()
    
    for id,email in legacy_set :
        if (email not in blacklist) :
            clean_legacy_set.add(id)


    lost_set = clean_legacy_set - modern_set
    ghost_set = modern_set - clean_legacy_set

    result = (lost_set,ghost_set)

    return result 


