import main
import pytest


def translator(lines):
    translated_array  = []
    for i in lines:
        to_translate = i
        translated  = GoogleTranslator(source='auto',target='en').translate(i)
        translated_array.append(translated)
    return translated_array

def test_functions():
        assert translator("Bonjour") == "hello"






