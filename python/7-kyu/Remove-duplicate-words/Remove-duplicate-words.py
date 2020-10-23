def remove_duplicate_words(s):
    phrase=s.split()
    seen = set()
    list = []
    result = ""
    for int in phrase:
        if int not in seen:
            seen.add(int)
            list.append(int)        
    #return (result.join(list))
    result = ' '.join(map(str, list))
    return result
