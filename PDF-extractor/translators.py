from deep_translator import GoogleTranslator


#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
def translator_into_english(sentence):
    return GoogleTranslator(source = 'it',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    return GoogleTranslator(source = 'auto',target = 'it').translate(sentence)


