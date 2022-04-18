
from collections import defaultdict
import nltk
import pdfplumber
import pandas as pd
from deep_translator import GoogleTranslator
import re
import operator
import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from nltk.corpus import words
import enchant
import concurrent.futures
from time import time
import os
from difflib import SequenceMatcher
from nltk.translate.bleu_score import SmoothingFunction



def flatten_list(_2d_list):
    new_list = []
    for i in _2d_list:
        for j in i:
            new_list.append(j)
    return new_list






#function to test different regex expressions
#so findall definitely works for matching aceented characters
#problem is with the pdf extractor that we are using
def test_regex():
    matched = (re.findall('é','hé'))
    print("matched",matched)



#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
def translator(lines):
    print("about to translate the array")
    translated_array  = []
    for i in lines:
        to_translate = i
        translated  = GoogleTranslator(source='auto',target='en').translate(i)
        translated_array.append(translated)
    print("translated")
    return translated_array

'''
attempt to implement concurrency 
def translation_work(line):
    translated  = GoogleTranslator(source='auto',target='en').translate(line)
    return translated

def translator_with_concurrency(lines):
    print("about to start concurrency")
    translated_array = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for line in lines:
            futures.append(executor.submit(translation_work(line)))
        for future in concurrent.futures.as_completed(futures):
            translated_array.append(future.result())

    return translated_array

'''



#cleans text from any whitesace and can later be used to remove punctuation if necessary
def clean(text):
    text = re.sub('\n','',str(text))
    text = re.sub('\n',' ',str(text))
    return text



#contains the kwyrods for each poverty question and translates them into the target language - change later so that
#you can change the language we are using
def keywords():

    global questions_to_keywords
    questions_to_keywords={
        "Can your whole household afford to go for a week’s annual holiday, away from home?":["vacation","holiday","holiday residence","residence"],
        "Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?":["vegetarian"],
        "Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?":["expense","costs"],
        "Does your household have a telephone(fixed landline or mobile)?":["telephone","phone"],
        "Does your household have a color TV?":["colour TV","colour television"],
        "Does the household have a washing machine? ":["washing machine"],
        "Does your household have a car/van for private use? ":["van","autobus"],
        "Do you have any of the following problems with your dwelling/accommodation? ":["dwelling","lodging"],
        "Can your household afford to keep its home adequately warm?":["warm","heat"]
    }

    translated_keywords_dict = defaultdict()
    for key in questions_to_keywords.values():
        for item in key:
            translated_keywords_dict[GoogleTranslator(source='en', target='french').translate(item)] = []
    return (translated_keywords_dict)




def check_keywords(array_of_questions):
    relevant_questions =[]
    array_of_keywords = ["holiday","vacation","holiday residence","residence","vegetarian","expense","costs","telephone","phone","colour TV","colour television","washing machine", "van", "dwelling","lodging","warm","heat"]
    for question in array_of_questions:
        if any(word in question for word in array_of_keywords):
            relevant_questions.append(question)
        else:
            continue
    return relevant_questions



#print(check_keywords(["do you have a van?","do you have a colour TV", "what is your name","washing machine?"]))
#should return ["do you have a van?","do you have a colour TV","washing machine?"]

#iterates through an array which contains page numbers, extracts each quesiton from that page, translates them into english,
#adds to an array, cleans data and adds to final array



def new_translate_document(pages):
    pdf1 = pdfplumber.open("france.pdf")
    pages = pages
    clean_foreign_questions = set()
    translated_questions = []
    for number in pages:
        p1 = pdf1.pages[number]
        text = p1.extract_text()
        text = clean(text)
        sentences = nltk.sent_tokenize(text)
        for item in sentences:
            if item[-1] == "?":
                clean_foreign_questions.add(item)

    translated_questions.append(translator(clean_foreign_questions))

    return translated_questions



#BLEU allows to compare set of references with a candidate,
# so if you want to use it you should set the list of lists of sentences as a list of references.
# In other words, even if you take only one reference it should be a list of lists
# (in my example reference should be [reference]:
#reference: https://stackoverflow.com/questions/68926574/i-compare-two-identical-sentences-with-bleu-nltk-and-dont-get-1-0-why

##TESTING BLEU VS SIMILAR SCORE API


def bleu_implementation(array_of_questions_to_compare,original_question):

    max_score = 0
    question_name = ""
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question)
        if score == 1:
            max_score = 1
            question_name += item
        elif score > max_score:
            max_score = score
            question_name += item

    return max_score
##bleu_implementation(["hello my name is lipples","hello my name is lipi"],"hello my name is lipi", )



#works quite well maybe run it through this first
def similar(string1,string2):
    return SequenceMatcher(None,string1,string2).ratio()
def similar_sentence(question,target_list):
    return max(target_list,key=lambda str:similar(question,str))
#test_array = ["do you have a washing machine", "do you have a car"," cars are nice","i want a car","i want a washing machine"]
#question = "do you have a washing machine"
#print(similar_sentence(question,test_array))


def remove_brackets(keywords_list):
    tidied_list  = []
    for keyword_question in keywords_list:
        tidied_list.append(re.sub("[\(\[].*?[\)\]]", "", keyword_question))

    return tidied_list




def main():
    translated_keywords = keywords().keys()
    pages = set()
    pdf = pdfplumber.open("france.pdf")
    print("about to find pages")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)
    print(pages,"found the page numbers and about to translate")
    #test_list = [45,73,79,107,158,159,161,164,165,232,251,273]
    clean_translations = flatten_list(new_translate_document(list(pages)))
    #clean_translations = flatten_list(new_translate_document(test_list))
    print("translated")
    #print(clean_translations)
    #dictionary of quesion to its highest BLEU score
    print("about to go through the words and check taht they are in english ")
    question_to_scores = defaultdict()
    words = set(nltk.corpus.words.words())
    new_list = []
    for question in clean_translations:
        new_list.append(" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question))\
                if w.lower() in words or not w.isalpha()))
    keywords_list = check_keywords(new_list)
    updated_keywords_list = remove_brackets(keywords_list)
    print("removed brackets")
    return updated_keywords_list


# CODE TO CONVERT INTO A DATAFRAME LATER ON
    #d = {'Cleaned Questions':keywords_list}
    #DftranslatedDoc=pd.DataFrame(data =d)
    #DftranslatedDoc.to_csv(os.getcwd() + r'final_output.csv',index = False)
    #print("outputted as CSV file ")
#convert to a mysql file ready for website



#main()





def bleu_implementation(original_question,array_of_questions_to_compare):



    scores = defaultdict()
    question_name = ""
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question,smoothing_function=SmoothingFunction().method1)
        scores[score] = item
    max_score = max(scores.keys())
    print(scores)
    return scores[max_score]



davids_questions_to_match = ["Can your whole household afford to go for a week’s annual holiday, away from home?","Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?","Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?","Does your household have a telephone(fixed landline or mobile)?","Does your household have a color TV?","Does the household have a washing machine? ","Does your household have a car/van for private use? ","Do you have any of the following problems with your dwelling/accommodation? ","Can your household afford to keep its home adequately warm? "]
matched_questions = defaultdict()

array_of_questions = main()
for question in davids_questions_to_match:
    #matched_questions[question] = similar_sentence(question,array_of_questions)
    matched_questions[question] = bleu_implementation(question,array_of_questions)
print("about to print matched items")
for item in matched_questions.items():
    print(item)




















# concurrent main


'''
if __name__ == "__main__":
    translated_keywords = keywords().keys()
    pages = set()
    pdf = pdfplumber.open("france.pdf")
    print("about to find pages")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)
    print(pages,"found the page numbers and about to translate")
    test_list = [45,73,79,107,158,159,161,164,165,232,251,273]
    with ProcessPoolExecutor(max_workers=100) as pool:
        result = pool.map(new_translate_document, test_list)
    print(result)
    clean_translations = flatten_list(result)
    #clean_translations = flatten_list(new_translate_document(test_list))
    print("translated")
    #print(clean_translations)
    #dictionary of quesion to its highest BLEU score
    print("about to go through the words and check taht they are in english ")
    question_to_scores = defaultdict()
    words = set(nltk.corpus.words.words())
    new_list = []
    for question in clean_translations:
        new_list.append(" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question))\
                if w.lower() in words or not w.isalpha()))

    keywords_list = check_keywords(new_list)





'''







