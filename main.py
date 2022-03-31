'''
This is the functioning code.
following steps:

    1. Find all of the words that are not part of the english dictionary and remove them, make sure this method works fully
    2. test the BLEU function again and test that it works
    3. see how many questions are actually being narrowed down
    4. make sure this all works before adding the concurrency, as we need a functioning database first

'''


from collections import defaultdict
from IPython.display import display
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
    translated_array  = []
    for i in lines:
        to_translate = i
        translated  = GoogleTranslator(source='auto',target='en').translate(i)
        translated_array.append(translated)
    return translated_array






#cleans text from any whitesace and can later be used to remove punctuation if necessary
def clean(text):
    text = re.sub('\n','',str(text))
    text = re.sub('\n',' ',str(text))
    #removing punctuation
    #text = re.sub(r'[^\w\s]','',text)
    return text


#contains the kwyrods for each poverty question and translates them into the target language - change later so that
#you can change the language we are using
def keywords():

    global questions_to_keywords
    questions_to_keywords={
        "holiday":"Can your whole household afford to go for a week’s annual holiday, away from home?",
        "vegetarian":"Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?",
        "expense": "Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?",
        "telephone":"Does your household have a telephone(fixed landline or mobile)?",
        "colour TV":"Does your household have a color TV?",
        "washing machine":"Does the household have a washing machine? ",
        "van":"Does your household have a car/van for private use? ",
        "dwelling":"Do you have any of the following problems with your dwelling/accommodation? ",
        "warm":"Can your household afford to keep its home adequately warm?  "
    }
    translated_keywords_dict = defaultdict()
    for key in questions_to_keywords.keys():
        translated_keywords_dict[GoogleTranslator(source='en', target='french').translate(key)] = []
    return translated_keywords_dict




#iterates through an array which contains page numbers, extracts each quesiton from that page, translates them into english,
#adds to an array, cleans data and adds to final array
def translate_document(pages):
    pdf1 = pdfplumber.open("france.pdf")
    translated_array = []
    #pages = list(pages)
    # writing page 161 will translate page 162
    pages= pages
    for number in pages:
        p1 = pdf1.pages[number]
        im = p1.to_image()
        text = p1.extract_text()
        text = clean(text)
        #text = re.split('[?]',text)
        text = re.findall('(?<=[\?\.\!]\s)[^\?\n\.]+?\?',text)
        clean_sent  = []
        for sent in text:
            clean_sent.append(sent)
            #translated_array.append(clean_sent)
        translated_array.append(translator(clean_sent))
    return translated_array




#BLEU allows to compare set of references with a candidate,
# so if you want to use it you should set the list of lists of sentences as a list of references.
# In other words, even if you take only one reference it should be a list of lists
# (in my example reference should be [reference]:
#reference: https://stackoverflow.com/questions/68926574/i-compare-two-identical-sentences-with-bleu-nltk-and-dont-get-1-0-why





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



#reference : https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python



## returns true if a work is in English dictionary with british spelling
def check_word(word):
    d = enchant.Dict("en_GB")
    if d.check(word):
        return True
    return False


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
    #print(pages)
    print("found the page numbers and about to translate")
    clean_translations = flatten_list(translate_document(list(pages)))
    print("translated")

    #dictionary of quesion to its highest BLEU score
    print("about to go through the words and check taht they are in english ")
    question_to_scores = defaultdict()
    print(clean_translations)
    words = set(nltk.corpus.words.words())
    new_list = []
    for question in clean_translations:
        new_list.append(" ".join(w for w in nltk.wordpunct_tokenize(str(question)) \
                if w.lower() in words or not w.isalpha()))

    print(new_list)
    #for question in questions_to_keywords.values():
        #question_to_scores[question] = bleu_implementation(clean_translations,question)
    #print(question_to_scores)


# CODE TO CONVERT INTO A DATAFRAME LATER ON
    d = {'Translated Questions':clean_translations,'Cleaned Questions':new_list}
    DftranslatedDoc=pd.DataFrame(data =d)
    display(DftranslatedDoc)
#convert to a mysql file ready for website


main()







#NEXT SECTION






'''

from collections import defaultdict
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
import time



pdf = pdfplumber.open("france.pdf")

def flatten_list(_2d_list):
    return np.ravel(_2d_list).tolist()



#function to test different regex expressions
#so findall definitely works for matching aceented characters
#problem is with the pdf extractor that we are using
def test_regex():
    matched = (re.findall('é','hé'))
    print("matched",matched)



#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
def translator(lines):
    translated_array  = []
    for i in lines:
        to_translate = i
        translated= GoogleTranslator(source='auto',target='en').translate(i)
        translated_array.append(translated)
    return translated_array






#cleans text from any whitesace and can later be used to remove punctuation if necessary
def clean(text):
    text = re.sub('\n','',str(text))
    text = re.sub('\n',' ',str(text))
    #removing punctuation
    #text = re.sub(r'[^\w\s]','',text)
    return text


#contains the kwyrods for each poverty question and translates them into the target language - change later so that
#you can change the language we are using
def keywords():

    global questions_to_keywords
    questions_to_keywords={
        "holiday":"Can your whole household afford to go for a week’s annual holiday, away from home?",
        "vegetarian":"Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?",
        "expense": "Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?",
        "telephone":"Does your household have a telephone(fixed landline or mobile)?",
        "colour TV":"Does your household have a color TV?",
        "washing machine":"Does the household have a washing machine? ",
        "van":"Does your household have a car/van for private use? ",
        "dwelling":"Do you have any of the following problems with your dwelling/accommodation? ",
        "warm":"Can your household afford to keep its home adequately warm?  "
    }
    translated_keywords_dict = defaultdict()
    for key in questions_to_keywords.keys():
        translated_keywords_dict[GoogleTranslator(source='en', target='french').translate(key)] = []
    return translated_keywords_dict

def actual_translation_work(page_number,pdf1):
    p1  = pdf1.pages[page_number]
    im = p1.to_image()
    text = p1.extract_text()
    text = clean(text)
    text = re.findall('(?<=[\?\.\!]\s)[^\?\n\.]+?\?',text)
    clean_sent = []
    for sent in text:
        clean_sent.append(sent)
    translated_cleaned = translator(clean_sent)
    return translated_cleaned

def translate_document(pages,pdf1):
    translated_array = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for page in pages:
            futures.append(executor.submit(actual_translation_work, page_number=page, pdf1=pdf))
        for future in concurrent.futures.as_completed(futures):
            translated_array.append(future.result())
    return translated_array


#iterates through an array which contains page numbers, extracts each quesiton from that page, translates them into english,
#adds to an array, cleans data and adds to final array



#BLEU allows to compare set of references with a candidate,
# so if you want to use it you should set the list of lists of sentences as a list of references.
# In other words, even if you take only one reference it should be a list of lists
# (in my example reference should be [reference]:
#reference: https://stackoverflow.com/questions/68926574/i-compare-two-identical-sentences-with-bleu-nltk-and-dont-get-1-0-why





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



#reference : https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python



## returns true if a work is in English dictionary with british spelling 
def check_word(word):
    print("here")
    d = enchant.Dict("en_GB")
    if d.check(word):
        return True
    return False


def main():
    translated_keywords = keywords().keys()
    pages = set()
    print("here- getting pages")
    #pdf = pdfplumber.open("france.pdf")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)
    #print(pages)
    print('here2- got the pages')
    translated = translate_document(list(pages),pdf)
    clean_translations = flatten_list(translated)
    print('here3 - finished transalteding ')



    #CONVERT INTO A DATAFRAME LATER ON
    d = {'Translated Questions':clean_translations}
    DftranslatedDoc=pd.DataFrame(data =d)
    DftranslatedDoc.to_mysql('out_translation.csv',index=False)





#hopefully then we have a df of only questions whcih we can use to calculate the BLEU score
main()
THIS SECTION IS COMMENTED OUT
#dictionary of quesion to its highest BLEU score
question_to_scores = defaultdict()
for question in clean_translations:
    print(question)
    words_list = question.split('',word)
    print(words_list)
    #for word in words_list:
    #if not check_word(word):
    #  words_list.remove(word)
    #question = words_list.join(' ')
#for question in questions_to_keywords.values():
#question_to_scores[question] = bleu_implementation(clean_translations,question)
# print(question_to_scores)

'''


























