def solution(s):
    result = ''
    for char in s:
        if char.isupper() is True:
            result = result + ' ' + char
        else:
            result = result + char
    return result
