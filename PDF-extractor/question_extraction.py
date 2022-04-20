from collections import defaultdict
import nltk
import pdfplumber
import re
import translators
import text_preprocessing


def translate_keywords():
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
            translated_keywords_dict[translators.translator_into_foreign(item)] = []
    return (translated_keywords_dict)







def find_and_translate_questions(pages):
    pdf1 = pdfplumber.open("italy.pdf")
    clean_foreign_questions = set()
    translated_questions = defaultdict()
    for number in pages:
        p1 = pdf1.pages[number]
        text = text_preprocessing.remove_whitespace(p1.extract_text())
        sentences = nltk.sent_tokenize(text)
        for item in sentences:
            if item[-1] == "?":
                clean_foreign_questions.add(item)
    for item in clean_foreign_questions:
        key_to_add = translators.translator_into_english(item)
        translated_questions[key_to_add] = item

    return translated_questions







def preprocess_translated_questions():
    translated_keywords = translate_keywords().keys()
    pages = set()
    pdf = pdfplumber.open("italy.pdf")
    for word in translated_keywords:
        word = word.lower()
        for i in range(0,len(pdf.pages)):
            page_number = pdf.pages[i]
            Text = page_number.extract_text()
            if re.findall(word,Text,re.IGNORECASE):
                pages.add(i)
    clean_translations = find_and_translate_questions(list(pages))
    words = set(nltk.corpus.words.words())
    new_dictionary = defaultdict()
    for question in clean_translations.keys():
        item = (" ".join(w.lower() for w in nltk.wordpunct_tokenize(str(question)) \
                         if w.lower() in words or not w.isalpha()))
        new_dictionary[item] = clean_translations[question]
    keywords_questions = text_preprocessing.check_keywords(clean_translations)
    updated_keywords_list = text_preprocessing.remove_brackets(keywords_questions)
    return updated_keywords_list



