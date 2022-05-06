from collections import defaultdict
import re

#cleans text from any whitespace and can later be used to remove punctuation if necessary
def remove_whitespace(text):
    text = re.sub('\n','',str(text))
    text = re.sub('\n',' ',str(text))
    return text



## new remove brackets function
def remove_brackets(input_dictionary):
    print("removing brackets")
    tidied_dictionary = defaultdict()
    for keyword_question in input_dictionary.keys():
        tidied_dictionary[re.sub("[\(\[].*?[\)\]]", "", keyword_question)] = input_dictionary[keyword_question]
    return tidied_dictionary




## new def check keywords
def check_keywords(input_dictionary):
    print("Checking keywrods")
    relevant_questions =  defaultdict()
    array_of_keywords = ["holiday","vacation","holiday residence","residence","vegetarian","expense","costs",
                         "telephone","phone","colour TV","colour television","washing machine", "van", "dwelling","lodging","warm",
                         "heat","heating","warmth","problems","neighbourhood","encounter","postal","banking","services",
                         "mobile phone","phone","mobile","shoes","all-weather","fitting",
                         "second-hand","clothes","drink","meal","month","relatives","sport","cinema","concert","small",
                         "money","consult","small","money","consult","dentist","ophthalmologist","specialist","doctor",
                         "second hand","clothes","pairs","fitting shoes","all-weather","fruits","vegetables","three","meals"
        ,"meat","chicken","fish","books","bicycle","roller skates","baby","toys","building blocks","board games",
                         "computer games","swimming","instrument","birthdays","name days","religious events","trips",
                         "school trips","school events","study","homework","outdoor","play","safely"]
    for question in input_dictionary.keys():
        if any(word in question for word  in array_of_keywords):
            relevant_questions[question] = input_dictionary[question]
    return relevant_questions

