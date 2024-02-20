def returnWords(translate_word, languague):
    with open('translator.txt', 'r') as f:
        for par in f:
            words = par.split()
            source, target = words[0], words[2]

            if languague == "I" and source == translate_word:
                return target
            elif languague == "E" and target == translate_word:
                return source

    return ""

def saveWords(palabra_espanhol, english_word):
    dic = "{} {}".format(palabra_espanhol, english_word)
    with open('translator.txt', 'a') as f:
        f.write('\n' + dic)