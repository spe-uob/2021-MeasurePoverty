from deep_translator import GoogleTranslator




def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)



