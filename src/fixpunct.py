def fixpunctuation(sentence):
    sentence=sentence.replace(' !', "!")
    sentence=sentence.replace(' ?', "?")
    sentence=sentence.replace(' ,', ",")
    sentence=sentence.replace(' .', ".")
    sentence=sentence.replace(' :', ":")

    return sentence
