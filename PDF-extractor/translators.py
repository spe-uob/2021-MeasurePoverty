from deep_translator import GoogleTranslator


#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
import keyword_identifiers


def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    #CHANGE THE LANGUAGE
    return GoogleTranslator(source = 'en',target = 'fr').translate(sentence)


def choose_translator(input,sentence):

    target = keyword_identifiers.language_dict[input.lower()]
    return GoogleTranslator(source = 'en', target = target).translate(sentence)


