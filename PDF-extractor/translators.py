from deep_translator import GoogleTranslator
from deep_translator import MicrosoftTranslator
from deep_translator import DeepL
#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
import keyword_identifiers
language = input("input lanuage")


def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    #CHANGE THE LANGUAGE

    target = keyword_identifiers.translator_dict[language]
    return GoogleTranslator(source = 'en',target = target).translate(sentence)


'''

def choose_translator (sentence):
    target = keyword_identifiers.translator_dict[language.lower()]
    if translator.lower() == "a":
        return GoogleTranslator(source = 'en', target = target).translate(sentence)
    elif translator.lower() == "b":
        return MicrosoftTranslator(source = 'en', target = target).translate(sentence)
    elif translator.lower() == "c":
        return DeepL(source = 'en', target = target).translate(sentence)


'''
