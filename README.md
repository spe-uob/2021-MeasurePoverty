# MeasurePoverty 2021/2022



## Overview
Organizaton:University of Bristol working with UNICEF

Client: Dr David Gordon



### Context 

The Bristol Poverty Institue(University of Bristol) is working with UNICEF to develop a short question module to help improve the measurement of child and adult poverty in countries. 
The measure poverty project aims to match questions 


Scrape the relevant data from the questionnaires of each country in EUROSTAT and automate the identification of the conceptually translated question text in each language. Upon completion, construct and populate a multilingual database, and upload results on the web.


### User Stories 




|  User | Story |   
|------ |-------|
|   Researcher    | As a researcher,  I want access to the questions from foreign questionnaires, but translated into English    |  
|   Member of UNICEF |  As a member of UNICEF,  I want access to the questions from foreign questionnaires, but translated into English to be able to check which countries ask all the required questions |   
| University student | I want to be able to use the poverty questions asked to aid my studies    |
|Dr David Gordon| ? |


## User Guide/Deployment 


To access the website to view the poverty questions, use the following link

http://2021-measure-poverty.vercel.app/

The user is able to choose a country, and see the pages which contain the poverty questions, as well as the poverty questions in english and the native language


## Developer/Contribution Guide 

### Manual setups

#### Requirements
It is essential to have python 3.7+ (due to pyenchant) and pip installed on your device. 
To run the source code, run the following to install the necessary libraries:


```
pip install --user -U nltk
pip install --user -U numpy
pip install pdfplumber 
pip install deep-translator
pip install regex 
pip install pyenchant
```

To be able to determine which words are part of the English dictionary, we have used the pyenchant library.  

To install this on linux, do the following on command line:


```
pip install enchant2
```

Throughout our code, we make use of nltk datasets. To install, open python3 on commandline and run the following:

```
>>>import nltk
>>>nltk.download("punkt")

```
To install this, run python and type the following into the command line:

```
brew update
brew install enchant
```

In the event of any difficulties while installing pyenchant:


https://pyenchant.github.io/pyenchant/install.html







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
https://aclanthology.org/P02-1040.pdf

text pre-processing:
https://www.analyticsvidhya.com/blog/2021/09/essential-text-pre-processing-techniques-for-nlp/


NLP keywords extraction:
https://www.analyticsvidhya.com/blog/2022/03/keyword-extraction-methods-from-documents-in-nlp/


NLP topic modelling: 
https://www.analyticsvidhya.com/blog/2021/05/topic-modelling-in-natural-language-processing/

Concurrency:




## License 
MIT License
