#from matching_functions import bleu_implementation
from text_preprocessing import *
#from translators import *
#from question_extraction import *
from BLEU_matching import *

#functions from main.py
def test_bleu_implementation():
        assert bleu_implementation(["how are you?"],["how old are you?","how are you?"]) == "how are you?"


#functions from text_preprocessing.py
def test_remove_whitespace():
        assert remove_whitespace("clea\nn") == "clean"
        assert remove_whitespace("clean\n clean") == "clean clean"


def test_removebrackets():
        in_dict= {"(question 111)Does your household have a car/van for private use? ":["van","car","vehicle"]}
        assert remove_brackets(in_dict) == {'Does your household have a car/van for private use? ': ['van', 'car', 'vehicle']}

def test_checkkeywords():
        assert check_keywords({"How are you?":["you"],"Can your whole household afford to go for a week's annual holiday, away from home?":["vacation","holiday","holiday residence","residence"]})=={"Can your whole household afford to go for a week's annual holiday, away from home?": ['vacation', 'holiday', 'holiday residence', 'residence']}

'''
#functions from translators.py
def test_translatorintoenglish():
        assert translator_into_english("Ich möchte diesen Text übersetzen!") == "I want to translate this text!"

#no functions from keyword_identifiers.py need to be tested

#functions from question_extraction.py
def test_filter_non_words():
        assert filter_non_words(({"Do you have a fanzhaoyang":["car"],"Do you have a car":["car"],"DO you have a car":["car"]})) \
         == {'do you have a': ['car'], 'do you have a car': ['car']}
'''
