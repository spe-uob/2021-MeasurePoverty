# 2021-MeasurePoverty

## Deployment
http://2021-measure-poverty.vercel.app/

## Overview
Organizaton:University of Bristol working with UNICEF

Client: Dr David Gordon



### Context 

The Bristol Poverty Institue(University of Bristol) is working with UNICEF to develop a short question module to help improve the measurement of child and adult poverty in countries. 
The measure poverty project aims to match questions 


Scrape the relevant data from the questionnaires of each country in EUROSTAT and automate the identification of the conceptually translated question text in each language. Upon completion, construct and populate a multilingual database, and upload results on the web.


### User Stories 




Flow Steps:
1. Scrape the annual questionnaires from each country from the EUROSTAT website
2. Translate the questions by Google translator, match the same or similar question of different languages through keywords identification and statistical lexical matching.
3. Construct and populate a multilingual question database.
4. Upload and make the results available on the web.





## User Guide/Deployment 
The using logic:
For users, choose one language -> choose one question -> show the question in the chosen question -> (optional) show the whole pdf in the chosen language

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



#### Running





## Developer Guide



## Architecture & Workflow 

### architecture

### workflow 

## References / Resources


## Contribution Guide 

