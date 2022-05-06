from deep_translator import GoogleTranslator, PonsTranslator
import keyword_identifiers
import question_extraction


def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    #CHANGE THE LANGUAGE
    target = keyword_identifiers.translator_dict[question_extraction.language]
    return GoogleTranslator(source = 'en',target = target).translate(sentence)

