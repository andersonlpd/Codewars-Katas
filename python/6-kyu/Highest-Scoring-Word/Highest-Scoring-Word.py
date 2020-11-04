def high(x):
    PreResult = FinalResult = 0
    for word in x.split():
        PreResult = sum(ord(char) - 96 for char in word)
        if PreResult > FinalResult: 
            FinalResult = PreResult
            FinalWord = word
    return FinalWord
