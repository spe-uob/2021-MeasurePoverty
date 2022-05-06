from deep_translator import GoogleTranslator
from deep_translator import MicrosoftTranslator
from deep_translator import DeepLTranslator

#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
import keyword_identifiers


def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    #CHANGE THE LANGUAGE
    return GoogleTranslator(source = 'en',target = 'fr').translate(sentence)


def choose_translator (translator,language,sentence):
    target = keyword_identifiers.language_dict[language.lower()]
    if translator.lower() == "A":

        return GoogleTranslator(source = 'en', target = target).translate(sentence)
    elif translator.lower() == "B":
        return MicrosoftTranslator(source = 'en', target = target).translate(sentence)

    elif translator.lower() == "C":
        return DeepLTranslator(source = 'en', target = target).translate(sentence)

