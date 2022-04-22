from main import *

def test_bleu_implementation():
        assert bleu_implementation(["how are you?"],["how old are you?","how are you?"]) == ["how are you?"]


'''def test_translator():
        assert translator(["bonjour"]) == ["good morning"]

def test_flattenlist():
        assert flatten_list([["a","b"],["c","d"]]) == ["a","b","c","d"]

def test_clean():
        assert clean("clea\nn") == "clean"
        assert clean("clean \n clean") == "clean  clean"'''





