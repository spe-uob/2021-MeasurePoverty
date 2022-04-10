from deep_translator import GoogleTranslator

to_translate = "je veux traduire"

translated = GoogleTranslator(source='auto',target='en').translate(to_translate)
print(translated)