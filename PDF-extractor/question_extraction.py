from collections import defaultdict
import nltk
import pdfplumber
import re
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
from deep_translator import GoogleTranslator,PonsTranslator
import keyword_identifiers
import translators
import text_preprocessing


def choose_translator(translator_choice,sentence):
    target = keyword_identifiers.translator_dict[language.lower()]
    if translator_choice.lower() == "a":
        return GoogleTranslator(source = 'en', target = target).translate(sentence)
    elif translator_choice.lower() == "b":
        #return MicrosoftTranslator(source = 'en', target = target).translate(sentence)
        return PonsTranslator(source='en', target=target).translate(sentence)



def translate_keywords():
    translated_keywords_dict = defaultdict()
    for key in keyword_identifiers.questions_to_keywords.values():
        for item in key:
            translated_keywords_dict[choose_translator(translator_choice,item)] = []
    return (translated_keywords_dict)


def tokenize_and_translate_questions(pages):
    print("tokenizing")
    translated_questions = defaultdict()
    for number in pages:
        p1 = pdf.pages[number]
        text = text_preprocessing.remove_whitespace(p1.extract_text())
        sentences = nltk.sent_tokenize(text)
        for item in sentences:
            if item[-1] == "?":
                translated_questions[translators.translator_into_english(item)] = item
    return translated_questions


def filter_non_words(input_dictionary):
    print("Filtering non words")
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



def bleu_implementation(original_question,array_of_questions_to_compare):
    scores = defaultdict()
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question,smoothing_function=SmoothingFunction().method1)
        scores[score] = item
    max_score = max(scores.keys())
    return scores[max_score]


def group_questions_by_keyword(ungrouped_dictionary):
    print("grouping questions")
    grouped_questions= defaultdict()
    for question in ungrouped_dictionary.keys():
        keyword_group = []
        keyword_list = ungrouped_dictionary[question]
        for translated_question in translated_questions_to_check.keys():
            if any(keyword in translated_question for keyword in keyword_list):
                keyword_group.append(translated_question)
        grouped_questions[question] = keyword_group


    return grouped_questions




#returns dictionary of david questoin to matched question in foreign language
def main():
    print("about to do the logics")
    keyword_to_translations = group_questions_by_keyword(keyword_identifiers.questions_to_keywords)
    matched_questions = defaultdict()
    for key,value in keyword_to_translations.items():
        if value == []:
            matched_questions[key] = ["not found"]
        else:
            matched_questions[key] = bleu_implementation(key,value)



    final_dataframe_dictionary = defaultdict()
    for davids_question in matched_questions.keys():
        if matched_questions[davids_question] == ["not found"]:
            final_dataframe_dictionary[davids_question] = "not found"
        else:
            final_dataframe_dictionary[davids_question] = translated_questions_to_check[matched_questions[davids_question]]


    return final_dataframe_dictionary



#MAIN TERMINAL FUNCTIONALITY
language = input("input language")
filename = input("Please enter the name of the questionnaire PDF:\n")
year = input("please input year")
print(f'You entered {filename} and please import the pdf file into the folder if its later than 2009 ')
pdf = pdfplumber.open(filename)
translator_choice = input("A-default google \n B-PONSTranslator")
translated_questions_to_check = find_and_preprocess_questions()
output_dict = main()
print(output_dict)





