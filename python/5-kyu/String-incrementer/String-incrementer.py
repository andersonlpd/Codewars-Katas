def increment_string(strng):
    Chars = strng.rstrip('0123456789') # Stripping the string deleting every rightmost number (foobar)
    Numbers = strng[len(Chars):] # Doing the opposite now to get everything that is a not a char
    if len(Numbers) == 0: return strng + '1' # If the string does not contain any number, add '1' to the string
    
    # Putting everything together.. Joining the characters with the number + 1. Zfill is used here to fill with zeros the int that is being incremented until it reaches the original length of the number.
    
    return Chars + str(int(Numbers)+1).zfill(len(Numbers))
