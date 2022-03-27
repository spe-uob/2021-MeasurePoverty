# 2021-MeasurePoverty



## Overview
Organizaton:University of Bristol working with UNICEF

Client: Dr David Gordon



### Context 

The Bristol Poverty Institue(University of Bristol) is working with UNICEF to develop a short question module to help improve the measurement of child and adult poverty in countries. 
The measure poverty project aims to match questions 


Scrape the relevant data from the questionnaires of each country in EUROSTAT and automate the identification of the conceptually translated question text in each language. Upon completion, construct and populate a multilingual database, and upload results on the web.


### User Stories 







## User Guide/Deployment 


To access the website to view the poverty questions, use the following link

http://2021-measure-poverty.vercel.app/

The user is able to choose a country, and see the pages which contain the poverty questions, as well as the poverty questions in english and the native language


## Developer Guide

### Manual setups

#### Requirements
It is essential to have python 3.9 and pip installed on your device. 
To run the source code, run the following to install the necessary libraries:


```
pip install --user -U nltk
pip install --user -U numpy
pip install pdfplumber 
pip install deep-translator
pip install regex 
```

To be able to determine which words are part of the English dictionary, we have used the NLTK data package "words". To install this, run python and type the following into the command line:

```
>>> import nltk
>>> nltk.download("words")
```






## Architecture & Workflow 

Our Approach:
1. Extract text from the questionnaire, translate into English, and identify questions based on whether they end with a quesiton mark
2. Narrow down the questions that contain the keywords that are included in the set list of poverty questions 
3. Use NLP and BLEU analysis to determinte the questions are poverty themed, and populate database
4. Upload and make the database available on the web, as well as open sourced for furture developments in the NLP algorithm 



### Architecture

### User Flowchart

## References / Resources
Most reference contained in source code.

BLEU theory/information:


## Contribution Guide 

## License 

