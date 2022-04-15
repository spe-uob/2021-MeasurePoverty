from main import *


def test_translator():
        assert translator(["good morning"]) == ["buenos días"]


def test_flattenlist():
        assert flatten_list([["a","b"],["c","d"]]) == ["a","b","c","d"]

def test_clean():
        assert clean("clea\nn") == "clean"
        assert clean("clean \n clean") == "clean  clean"

def test_bleu_implementation():
        assert bleu_implementation(["how are you heh?", "what should i eat?"], "bread is my pot") == 3.237552826118531e-78


