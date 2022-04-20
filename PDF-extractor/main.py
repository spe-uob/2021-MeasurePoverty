
from collections import defaultdict
import nltk
import pdfplumber
import pandas as pd
from deep_translator import GoogleTranslator
import re
from nltk.translate.bleu_score import sentence_bleu
from difflib import SequenceMatcher
from nltk.translate.bleu_score import SmoothingFunction

from IPython.display import display



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
            translated_keywords_dict[GoogleTranslator(source='en', target='it').translate(item)] = []
    return (translated_keywords_dict)





#print(check_keywords(["do you have a van?","do you have a colour TV", "what is your name","washing machine?"]))
#should return ["do you have a van?","do you have a colour TV","washing machine?"]





def translate_document(pages):
    pdf1 = pdfplumber.open("italy.pdf")
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
    pdf = pdfplumber.open("italy.pdf")

    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)

    #clean_translateions is a dictinoary of {english:french}
    clean_translations = translate_document(list(pages))

    words = set(nltk.corpus.words.words())
    new_dictionary = defaultdict()

    for question in clean_translations.keys():
        item = (" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question)) \
                         if w.lower() in words or not w.isalpha()))

        new_dictionary[item] = clean_translations[question]
    keywords_questions = check_keywords(clean_translations)
    updated_keywords_list = remove_brackets(keywords_questions)

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
    "Does the household have a washing machine?":["washing machine","washing","machine"],
    "Does your household have a car/van for private use?":["van","car","vehicle"],
    "Do you have any of the following problems with your dwelling/accommodation?":["dwelling","lodging"],
    "Can your household afford to keep its home adequately warm?":["warm","heat","heating","warmth"]
}


translated_questions_to_check = main()
keywords_to_translated_questions = defaultdict()
davids_questions_to_match = ["Can your whole household afford to go for a week’s annual holiday, away from home?","Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?","Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?","Does your household have a telephone(fixed landline or mobile)?","Does your household have a color TV?","Does the household have a washing machine?","Does your household have a car/van for private use?","Do you have any of the following problems with your dwelling/accommodation?","Can your household afford to keep its home adequately warm?"]


# keywords to translated questions has a list of the questions associated with each keyword, narrows down what to check for BLEU algorithm
for question in final_questions_to_keywords.keys():
    #x list is the lsit of questions to compare to davids quesiton that contains the same keyword
    x_list = []
    keyword_list = final_questions_to_keywords[question]
    for translated_question in translated_questions_to_check.keys():
        if any(keyword in translated_question for keyword in keyword_list):
            x_list.append(translated_question)
    keywords_to_translated_questions[question] = x_list



## goes thtrouhg each item in dictionary, calculating BLEU score for key vs value
# now that we have the matched questions, have to go into the translated_qustions_to_check and get the french version ie from main values
matched_questions = defaultdict()
for key,value in keywords_to_translated_questions.items():
    if value == []:
        matched_questions[key] = ["not found"]
    else:
        matched_questions[key] = bleu_implementation(key,value)
print(matched_questions)



## createing a dataframe of english questions to french questions
dataframe_dictionary = defaultdict()
for davids_question in matched_questions.keys():
    if matched_questions[davids_question] == ["not found"]:
        dataframe_dictionary[davids_question] = ["not found"]

    else:
        dataframe_dictionary[davids_question] = translated_questions_to_check[matched_questions[davids_question]]
print(dataframe_dictionary)
display(pd.DataFrame.from_dict(dataframe_dictionary))


















