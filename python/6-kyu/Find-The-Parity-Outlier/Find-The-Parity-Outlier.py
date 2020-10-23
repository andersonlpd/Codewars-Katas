def find_outlier(integers):
    result=[x for x in integers if x % 2 != 0]
    if len(result) == 1:
        return int(''.join(map(str, result)))
    else:
        result=[x for x in integers if x % 2 == 0]
        return int(''.join(map(str, result)))
