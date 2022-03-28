###adding NLP and testing- current testing methods
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


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list




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


def check_word(word):
    print("here")
    d = enchant.Dict("en_UK")
    if d.check(word):
        print("true")
    else:
        print("False")

check_word("hesdfsfgiuhsg")

def main():
    translated_keywords = keywords().keys()
    pages = set()
    pdf = pdfplumber.open("france.pdf")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)
    #print(pages)
    clean_translations = flatten_list(translate_document(list(pages)))

    #dictionary of quesion to its highest BLEU score
    question_to_scores = defaultdict()
    for question in questions_to_keywords.values():
        question_to_scores[question] = bleu_implementation(clean_translations,question)
    print(question_to_scores)


    #CONVERT INTO A DATAFRAME LATER ON
    #d = {'Translated Questions':clean_translations}
    #DftranslatedDoc=pd.DataFrame(data =d)
    #DftranslatedDoc.to_mysql('out_translation.csv',index=False)
    '''
        for column in DftranslatedDoc.iterrows():
        print(column)
        for word in column:
            #if word is not an english word then remove it from the sentence
            if word not in words.words():
                print("here")
                column = column.replace(word,'')
        #print(DftranslatedDoc[column])
            print("here 2 ")
        print("here", column)
    
    '''



#hopefully then we have a df of only questions whcih we can use to calculate the BLEU score
#main()







### NLP experimentation
'''
import pdfplumber
import pandas as pd
from deep_translator import GoogleTranslator
import PyPDF2
import re
import operator
import numpy as np

import nltk
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import stopwords

pdf = pdfplumber.open("france.pdf")

nltk.download('stopwords')
stop_words= stopwords.words('english') # can be changed to ('french')


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()



def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list




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



def main():
    translated_keywords = keywords().keys()
    pages = []
    pdf = pdfplumber.open("france.pdf")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.append(i)
    print(pages)
    clean_translations = flatten_list(translate_document(pages))
    #d = {'Translated Questions':translate_document(pages)}
    d = {'Translated Questions':clean_translations}
    DftranslatedDoc=pd.DataFrame(data =d)
    display(DftranslatedDoc)
    DftranslatedDoc.to_csv('out_translation.csv',index=False)


main()


lemmatizier= WordNetLemmatizer()
for index,row in DftranslatedDoc.iterows():
    filttered_sentence=[]
    sentence = row['col1']
    sentence = re.sub(r'[^\w\s]','',sentence)
    words=nltk.word_tokenize(sentence)
    words=[ w for rw in words if not w in stop_words]
    for word in words:
        filttered_sentence.append(lemmatizer.lemmatize(word))
    #print(filttered_sentence)
    data.ix[index,'col1'] = filttered_sentence






'''


### last version that works


'''
import pandas as pd
from deep_translator import GoogleTranslator
import PyPDF2
import re
import operator
import numpy as np

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list




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
    keyword_list = keywords().keys()
    for number in pages:
        p1 = pdf1.pages[number]
        im = p1.to_image()
        text = p1.extract_text()
        text = clean(text)
        #text = re.split('[?]',text)
        text = re.findall('(?<=[\?\.\!]\s)[^\?\n\.]+?\?',text)
        for sentence in text:
            y = any(x in sentence for x in keyword_list)
            if not y:
                text.remove(sentence)
        clean_sent  = []
        for sent in text:
            clean_sent.append(sent)
        #translated_array.append(clean_sent)
        translated_array.append(translator(clean_sent))
    return translated_array




def main():
    translated_keywords = keywords().keys()
    pages = []
    pdf = pdfplumber.open("france.pdf")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.append(i)
    print(pages)
    clean_translations = flatten_list(translate_document(pages))
    #d = {'Translated Questions':translate_document(pages)}
    d = {'Translated Questions':clean_translations}
    DftranslatedDoc=pd.DataFrame(data =d)
    display(DftranslatedDoc)
    DftranslatedDoc.to_csv('out_translation.csv',index=False)

main()








'''