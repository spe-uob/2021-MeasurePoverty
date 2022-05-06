from collections import defaultdict
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import question_extraction
import keyword_identifiers
import pandas as pd
import csv
import os.path




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









'''
firebase_config ={
        "apiKey": "AIzaSyASZ59fobXr6ovy8QQUX2mogFso22v5nQM",
        "authDomain": "measuredb.firebaseapp.com",
        "databaseURL": "https://measuredb-default-rtdb.firebaseio.com",
        "projectId": "measuredb",
        "storageBucket": "measuredb.appspot.com",
        "messagingSenderId": "298611251603",
        "appId": "1:298611251603:web:0d236cfa7d1926a552f066"
    }

firebase = pyrebase.initialize_app(firebase_config)
database = firebase.database()





foreign_dictionary = main()


    ##IF THE COUNTRY HAS ONE LANGUAGE
list_of_english_questions = list(foreign_dictionary.keys())
print(list_of_english_questions)
for i in range(len(list_of_english_questions)):
    english = list_of_english_questions[i]

        #CHANGE "FRENCH" TO THE FOREIGN LANGUAGE WE ARE TRANSLATING INTO
    upload = {
        #need language names here
        "french":foreign_dictionary[english],
        "english":english,
    }

    database.child("Belgium_2014").child("BelgiumQ"+str(i)).set(upload)

print("completed upload")

'''








'''
ADDING FIRST  LANGUGAE WITH ENGLISH QUESTIONS 
list_of_english_questions = list(foreign_dictionary.keys())
print(list_of_english_questions)
for i in range(len(list_of_english_questions)):
    english = list_of_english_questions[i]

    #CHANGE "FRENCH" TO THE FOREIGN LANGUAGE WE ARE TRANSLATING INTO
    upload = {
    #need language names here 
        "dutch":foreign_dictionary[english],
        "english":english,
    }

    database.child("Belgium_2009").child("BelgiumQ"+str(i)).set(upload)



ADDING A SECOND LANGUAGE
list_of_english_questions = list(foreign_dictionary.keys())
print(list_of_english_questions)
for i in range(len(list_of_english_questions)):
    english = list_of_english_questions[i]

    #CHANGE "FRENCH" TO THE FOREIGN LANGUAGE WE ARE TRANSLATING INTO
    upload = {
    #need language names here 
        "dutch":foreign_dictionary[english],
        #"english":english,
    }
    database.child("Belgium_2009").child("BelgiumQ"+str(i)).update(upload)

'''
