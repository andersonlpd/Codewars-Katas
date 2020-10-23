def order(sentence):

    Splitted = sentence.split() # Splitting the full string
    
    Dict = {} # Initializing the dictionaire
    result = [] # Initializing the result list
    
    for word in Splitted: # Iterating through every word in the splitted string
        for char in word: # Iterating through every char in word
            if char.isdigit() and int(char) <= 9: # If the char is an integer and between 1 and 9 
                Dict[char] = word # Increment the dict with the key being the char in the string and the value being the word
    
    for x in sorted(Dict): # Iterating through the sorted dict
        result.append(Dict[x]) # Increment the result list with every sorted value in the dict 
        
    
    return ' '.join(result) # Printing the result list
