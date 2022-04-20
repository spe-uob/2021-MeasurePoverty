
from collections import defaultdict
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
from IPython.display import display
import question_extraction





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


translated_questions_to_check = question_extraction.preprocess_translated_questions()
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


















