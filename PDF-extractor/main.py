from collections import defaultdict
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import question_extraction
import keyword_identifiers



translated_questions_to_check = question_extraction.find_and_preprocess_questions()


def bleu_implementation(original_question,array_of_questions_to_compare):
    scores = defaultdict()
    for item in array_of_questions_to_compare:
        score = sentence_bleu([item],original_question,smoothing_function=SmoothingFunction().method1)
        scores[score] = item
    max_score = max(scores.keys())
    return scores[max_score]

print(bleu_implementation(["how are you ?"],["how are you?","how is he?"]))




def group_questions_by_keyword(ungrouped_dictionary):
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
            final_dataframe_dictionary[davids_question] = ["not found"]

        else:
            final_dataframe_dictionary[davids_question] = translated_questions_to_check[matched_questions[davids_question]]


    return final_dataframe_dictionary



main()













