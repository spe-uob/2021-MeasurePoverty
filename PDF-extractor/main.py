
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









#function to test different regex expressions
#so findall definitely works for matching aceented characters
#problem is with the pdf extractor that we are using
def test_regex():
    matched = (re.findall('é','hé'))
    print("matched",matched)



#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
def translator(line):
    return GoogleTranslator(source = 'auto',target = 'en').translate(line)





#cleans text from any whitespace and can later be used to remove punctuation if necessary
def clean(text):
    text = re.sub('\n','',str(text))
    text = re.sub('\n',' ',str(text))
    return text



#contains the kwyrods for each poverty question and translates them into the target language - change later so that
#you can change the language we are using
def keywords():


    questions_to_keywords={
        "Can your whole household afford to go for a week’s annual holiday, away from home?":["vacation","holiday","holiday residence","residence"],
        "Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?":["vegetarian","meat","chicken","fish"],
        "Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?":["expense","costs"],
        "Does your household have a telephone(fixed landline or mobile)?":["telephone","phone"],
        "Does your household have a color TV?":["colour TV","colour television","colour","television","TV"],
        "Does the household have a washing machine? ":["washing machine","washing","machine"],
        "Does your household have a car/van for private use? ":["van","car","vehicle"],
        "Do you have any of the following problems with your dwelling/accommodation? ":["dwelling","lodging"],
        "Can your household afford to keep its home adequately warm?":["warm","heat","heating","warmth"]
    }

    translated_keywords_dict = defaultdict()
    for key in questions_to_keywords.values():
        for item in key:
            translated_keywords_dict[GoogleTranslator(source='en', target='french').translate(item)] = []
    return (translated_keywords_dict)





#print(check_keywords(["do you have a van?","do you have a colour TV", "what is your name","washing machine?"]))
#should return ["do you have a van?","do you have a colour TV","washing machine?"]





def new_translate_document(pages):
    pdf1 = pdfplumber.open("france.pdf")
    pages = pages
    clean_foreign_questions = set()
    translated_questions = defaultdict()
    for number in pages:
        p1 = pdf1.pages[number]
        text = p1.extract_text()
        text = clean(text)
        sentences = nltk.sent_tokenize(text)
        for item in sentences:
            if item[-1] == "?":
                clean_foreign_questions.add(item)

    for item in clean_foreign_questions:
        key_to_add = translator(item)
        translated_questions[key_to_add] = item

    return translated_questions


#BLEU allows to compare set of references with a candidate,
# so if you want to use it you should set the list of lists of sentences as a list of references.
# In other words, even if you take only one reference it should be a list of lists
# (in my example reference should be [reference]:
#reference: https://stackoverflow.com/questions/68926574/i-compare-two-identical-sentences-with-bleu-nltk-and-dont-get-1-0-why

##TESTING BLEU VS SIMILAR SCORE API





## new remove brackets function
def remove_brackets(keywords_questions):
    tidied_dictionary = defaultdict()
    for keyword_question in keywords_questions.keys():
        tidied_dictionary[re.sub("[\(\[].*?[\)\]]", "", keyword_question)] = keywords_questions[keyword_question]
    return tidied_dictionary

## new def check keywords
def check_keywords(new_dictionary):
    relevant_questions =  defaultdict()
    array_of_keywords = ["holiday","vacation","holiday residence","residence","vegetarian","expense","costs","telephone","phone","colour TV","colour television","washing machine", "van", "dwelling","lodging","warm","heat"]
    for question in new_dictionary.keys():
        if any(word in question for word  in array_of_keywords):
            relevant_questions[question] = new_dictionary[question]
        else:
            continue
    return relevant_questions




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
    #clean_translateions is a dictinoary of {english:french}
    clean_translations = new_translate_document(list(pages))
    print("translated")
    print("about to go through the words and check taht they are in english ")
    question_to_scores = defaultdict()
    words = set(nltk.corpus.words.words())
    new_dictionary = defaultdict()

    for question in clean_translations.keys():
        item = (" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question)) \
                         if w.lower() in words or not w.isalpha()))

        new_dictionary[item] = clean_translations[question]
    keywords_questions = check_keywords(clean_translations)
    updated_keywords_list = remove_brackets(keywords_questions)
    print(updated_keywords_list)
    return updated_keywords_list



#works quite well maybe run it through this first
def similar(string1,string2):
    return SequenceMatcher(None,string1,string2).ratio()
def similar_sentence(question,target_list):
    return max(target_list,key=lambda str:similar(question,str))
#test_array = ["do you have a washing machine", "do you have a car"," cars are nice","i want a car","i want a washing machine"]
#question = "do you have a washing machine"
#print(similar_sentence(question,test_array))



def bleu_implementation(original_question,array_of_questions_to_compare):
    scores = defaultdict()
    question_name = ""
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question,smoothing_function=SmoothingFunction().method1)
        scores[score] = item
    max_score = max(scores.keys())
    return scores[max_score]




final_questions_to_keywords={
    "Can your whole household afford to go for a week’s annual holiday, away from home?":["vacation","holiday","holiday residence","residence"],
    "Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?":["vegetarian","meat","chicken","fish"],
    "Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?":["expense","costs"],
    "Does your household have a telephone(fixed landline or mobile)?":["telephone","phone"],
    "Does your household have a color TV?":["colour TV","colour television","colour","television","TV"],
    "Does the household have a washing machine? ":["washing machine","washing","machine"],
    "Does your household have a car/van for private use? ":["van","car","vehicle"],
    "Do you have any of the following problems with your dwelling/accommodation? ":["dwelling","lodging"],
    "Can your household afford to keep its home adequately warm?":["warm","heat"]
}
translated_questions_to_check = main().keys()
keywords_to_translated_questions = defaultdict()
davids_questions_to_match = ["Can your whole household afford to go for a week’s annual holiday, away from home?","Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?","Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?","Does your household have a telephone(fixed landline or mobile)?","Does your household have a color TV?","Does the household have a washing machine? ","Does your household have a car/van for private use? ","Do you have any of the following problems with your dwelling/accommodation? ","Can your household afford to keep its home adequately warm? "]


for question in final_questions_to_keywords.keys():
    x_list = []
    keyword_list = final_questions_to_keywords[question]
    for translated_question in translated_questions_to_check:
        if any(keyword in translated_question for keyword in keyword_list):
            x_list.append(translated_question)
    keywords_to_translated_questions[question] = x_list


matched_questions = defaultdict()
for key,value in keywords_to_translated_questions.items():
    if value == []:
        matched_questions[key] = ["not found"]
    else:
        matched_questions[key] = bleu_implementation(key,value)
print(matched_questions)


'''

|- albanian: sq
|- amharic: am
|- arabic: ar
|- armenian: hy
|- azerbaijani: az
|- basque: eu
|- belarusian: be
|- bengali: bn
|- bosnian: bs
|- bulgarian: bg
|- catalan: ca
|- cebuano: ceb
|- chichewa: ny
|- chinese (simplified): zh-CN
|- chinese (traditional): zh-TW
|- corsican: co
|- croatian: hr
|- czech: cs
|- danish: da
|- dutch: nl
|- english: en
|- esperanto: eo
|- estonian: et
|- filipino: tl
|- finnish: fi
|- french: fr
|- frisian: fy
|- galician: gl
|- georgian: ka
|- german: de
|- greek: el
|- gujarati: gu
|- haitian creole: ht
|- hausa: ha
|- hawaiian: haw
|- hebrew: iw
|- hindi: hi
|- hmong: hmn
|- hungarian: hu
|- icelandic: is
|- igbo: ig
|- indonesian: id
|- irish: ga
|- italian: it
|- japanese: ja
|- javanese: jw
|- kannada: kn
|- kazakh: kk
|- khmer: km
|- kinyarwanda: rw
|- korean: ko
|- kurdish: ku
|- kyrgyz: ky
|- lao: lo
|- latin: la
|- latvian: lv
|- lithuanian: lt
|- luxembourgish: lb
|- macedonian: mk
|- malagasy: mg
|- malay: ms
|- malayalam: ml
|- maltese: mt
|- maori: mi
|- marathi: mr
|- mongolian: mn
|- myanmar: my
|- nepali: ne
|- norwegian: no
|- odia: or
|- pashto: ps
|- persian: fa
|- polish: pl
|- portuguese: pt
|- punjabi: pa
|- romanian: ro
|- russian: ru
|- samoan: sm
|- scots gaelic: gd
|- serbian: sr
|- sesotho: st
|- shona: sn
|- sindhi: sd
|- sinhala: si
|- slovak: sk
|- slovenian: sl
|- somali: so
|- spanish: es
|- sundanese: su
|- swahili: sw
|- swedish: sv
|- tajik: tg
|- tamil: ta
|- tatar: tt
|- telugu: te
|- thai: th
|- turkish: tr
|- turkmen: tk
|- ukrainian: uk
|- urdu: ur
|- uyghur: ug
|- uzbek: uz
|- vietnamese: vi
|- welsh: cy
|- xhosa: xh
|- yiddish: yi
|- yoruba: yo
|- zulu: zu




'''
