from collections import defaultdict
from nltk.translate.bleu_score import sentence_bleu
from difflib import SequenceMatcher
from pandas import *


def bleu_implementation(array_of_questions_to_compare,original_question):
    scores = defaultdict()
    question_name = ""
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question)
        scores[score] = item
    max_score = max(scores.keys())
    print(scores)
    return scores[max_score]




def similar(string1,string2):
    return SequenceMatcher(None,string1,string2).ratio()
def similar_sentence(question,target_list):
    return max(target_list,key=lambda str:similar(question,str))


#reading questions from the CSV file
data  = read_csv("PDF-extractorfinal_output.csv")
array_of_questions = data["Cleaned Questions"].tolist()
davids_questions_to_match = ["Can your whole household afford to go for a week’s annual holiday, away from home?","Can your household afford a meal with meat, chicken, fish(or vegetarian equivalent)?","Can your household afford an unexpected required expense(amount to be filled) and pay through its own resources?","Does your household have a telephone(fixed landline or mobile)?","Does your household have a color TV?","Does the household have a washing machine? ","Does your household have a car/van for private use? ","Do you have any of the following problems with your dwelling/accommodation? ","Can your household afford to keep its home adequately warm? "]



matched_questions = defaultdict()


#for question in davids_questions_to_match:
#    #matched_questions[question] = similar_sentence(question,array_of_questions)
#for item in matched_questions.items():
#    print(item)

for question in davids_questions_to_match:
    matched_questions[question] = bleu_implementation(array_of_questions,question)
for item in matched_questions.items():
    print(item)
