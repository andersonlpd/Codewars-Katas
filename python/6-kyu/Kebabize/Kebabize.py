def kebabize(string):
    result = ''
    for char in string:
        if char.isdigit():
            result = result
        elif char.isupper() is True:
            result = result + '-' + char
        else:
            result = result + char
    return result.lower() if result == '' else result[1:].lower() if result[0] == '-' else result.lower()
