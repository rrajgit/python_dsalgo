def splitter(string, delimiter):
    words = []   
    word = ""
    for c in string:
        if c != delimiter:
          word += c
        else:
          if word != "":
            words.append(word)
          word = "" 
    if word != "":
        words.append(word)

    return words
    
splitter('  cat   arc', ' ')
