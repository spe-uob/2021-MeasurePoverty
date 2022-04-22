from collections import defaultdict
import nltk
import pdfplumber
import re
import keyword_identifiers
import translators
import text_preprocessing
#import os
#from concurrent.futures import ProcessPoolExecutor
from multiprocessing.dummy import Pool as ThreadPool




pdf = pdfplumber.open("france.pdf")



def translate_keywords():


    translated_keywords_dict = defaultdict()
    for key in keyword_identifiers.questions_to_keywords.values():
        for item in key:
            translated_keywords_dict[translators.translator_into_foreign(item)] = []
    return (translated_keywords_dict)


def tokenize_and_translate_questions(pages):
    translated_questions = defaultdict()
    for number in pages:
        p1 = pdf.pages[number]
        text = text_preprocessing.remove_whitespace(p1.extract_text())
        sentences = nltk.sent_tokenize(text)
        ## this part needs to run faster
        for item in sentences:
            if item[-1] == "?":
                translated_questions[translators.translator_into_english(item)] = item

        ### until here
    return translated_questions

def parallel_tokenize_and_translate_questions(pages):
    translated_questions= defaultdict()
    # Create a threadpool with 3 threads
    pool = ThreadPool(3)
    # Run tokenize_and_translate_question on all 
    pool.map(tokenize_and_translate_questions, pages)
    pool.close()
    pool.join()
    return translated_questions






def filter_non_words(input_dictionary):
    words = set(nltk.corpus.words.words())
    new_dictionary = defaultdict()
    for question in input_dictionary.keys():
        item = (" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question)) \
                         if w.lower() in words or not w.isalpha()))
        new_dictionary[item] = input_dictionary[question]
    return new_dictionary



def find_and_preprocess_questions():
    translated_keywords = translate_keywords().keys()
    pages = set()
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            text = page_number.extract_text()
            if re.findall(word,text,re.IGNORECASE):
                pages.add(i)
    clean_translations = tokenize_and_translate_questions(list(pages))
    filtered_dictionary = filter_non_words(clean_translations)
    keywords_questions = text_preprocessing.check_keywords(filtered_dictionary)
    removed_brackets_list = text_preprocessing.remove_brackets(keywords_questions)
    return removed_brackets_list




