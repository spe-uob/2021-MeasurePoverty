from main import *
from text_preprocessing import *
from translators import *
from keyword_identifiers import *
from question_extraction import *

#functions from main.py
def test_bleu_implementation():
        assert bleu_implementation(["how are you?"],["how old are you?","how are you?"]) == ["how are you?"]

def test_groupedquestionsbykeywords():
        assert group_questions_by_keyword()

 #functions from text_preprocessing.py
        
def test_removewhitespace():
        assert remove_whitespace()
        
def test_removebrackets():
        assert remove_brackets()

def test_checkkeywords():
        assert check_keywords()

#functions from translators.py

def test_translatorintoenglish():
        assert translator_into_english()

def test_translatorintoforeign():
        assert translator_into_foreign()

#no functions from keyword_identifiers.py

#functions from question_extraction.py

#can someone assert the tests here



#def test_translator():
 #       assert translator(["bonjour"]) == ["good morning"]

#def test_flattenlist():
   #     assert flatten_list([["a","b"],["c","d"]]) == ["a","b","c","d"]

#def test_clean():
  #      assert clean("clea\nn") == "clean"
 #       assert clean("clean \n clean") == "clean  clean"'''





