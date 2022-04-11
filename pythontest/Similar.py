from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#for one sentence, find the highest score for it
def similar_sentence (question,target_list):
    string=question
    array=target_list
    return max(array, key=lambda str: similar(string, str))    