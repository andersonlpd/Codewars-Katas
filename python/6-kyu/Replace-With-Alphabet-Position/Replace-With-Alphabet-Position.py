def alphabet_position(text):
    return ' '.join(([str(ord(char) - 96) for char in text.replace(" ","").strip().lower() if char.isalpha() == True]))
