# 2021-MeasurePoverty

### PROJECT OVERVIEW
Scrape the relevant data from the questionnaires of each country in EUROSTAT and automate the identification of the conceptually translated question text in each language. Upon completion, construct and populate a multilingual database, and upload results on the web.



### STAKEHOLDERS

_-End users-_ Government workers/officials,experts in the National Statistics and academic research officials 

_-Organisation and System Managers-_ Professor David Gordon, group members in MeasurePoverty(Su Zhi Peen, Fanzhaoyang Lei, Rainand Tang,Lipi Chakraborty), UOB software engineering project course leaders

_-Organisation and system owners-_ Professor David Gordon, group members in MeasurePoverty(Su Zhi Peen, Fanzhaoyang Lei, Rainand Tang,Lipi Chakraborty), UOB software engineering project course leaders

_-General public who are affected by the system-_ people who fill out the questionnaire and do the survey_




### USER STORIES


As a researcher, I would like to view the questionnaires from the countries which are in a foreign language , so I need a program to provide the correct translation of each question.

As a client, I want to collect the answers of the questionnaires written in different languages so that I can easily match the same or similar questions of different languages.



Flow Steps:
1. Scrape the annual questionnaires from each country from the EUROSTAT website
2. Translate the questions by Google translator, match the same or similar question of different languages through keywords identification and statistical lexical matching.
3. Construct and populate a multilingual question database.
4. Upload and make the results available on the web.

### Structure
The using logic:
For users, choose one language -> choose one question -> show the question in the chosen question -> (optional) show the whole pdf in the chosen language

### Outline of Front-End and Back-End Implementations 

<img width="1350" alt="image" src="https://user-images.githubusercontent.com/72454289/145710454-b866d069-bfb2-47e5-80f1-c973cb69be0f.png">





