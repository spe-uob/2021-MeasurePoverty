#from main import *
#from text_preprocessing import *
from translators import *
#from keyword_identifiers import *
#from question_extraction import *

#functions from main.py
'''def test_bleu_implementation():
        assert bleu_implementation(["how are you?"],["how old are you?","how are you?"]) == "how are you?"
def test_groupedquestionsbykeywords():
        assert group_questions_by_keyword()

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
 # we currently dont test there two functions since we change the target languages for creating the database.
 # also these two functions are relatively simple to see the output instead of testing them

'''def test_translatorintoenglish():
        assert translator_into_english("Bonjour!") == "Hello!"

def test_translatorintoforeign():
        assert translator_into_foreign()'''

#no functions from keyword_identifiers.py

#functions from question_extraction.py











