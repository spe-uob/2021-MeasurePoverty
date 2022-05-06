import pdfplumber
import matching_functions
import pandas as pd



def option_A():
    filename = input("Please enter the name of the questionnaire PDF:\n")
    print(f'You entered {filename} and please make sure the pdf file is within the same folder as code')
    pdf = pdfplumber.open(filename)
    #do all logic with this filename
    return filename

def option_B():
    # do all logic with choice of translator
    output_dict = matching_functions.main()
    df = pd.DataFrame.from_dict(output_dict, orient="index")
    print(" translation complete, check folder for output spreadsheet")
    df.to_csv("experiment_translation.csv")


# change into forloop to check validity
input = input("OPTION A: upload questionnaire /n OPTION B: experiment with translator ")
if input.upper() == "A" :
    option_A()
elif input.upper() == "B":
    option_B()
    print('you chose option b')
else:
    print("invalid,rerun and input A or B")






