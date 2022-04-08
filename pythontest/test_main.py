import main
from pythontest.main import bleu_implementation

#def bleu_implementation(array_of_questions_to_compare,original_question):
    
#    max_score = 0
 #   question_name = ""
  #  for item in array_of_questions_to_compare:
   #     score = sentence_bleu([item],original_question)
    ##       max_score = 1
      #      question_name += item
       # elif score > max_score:
        #    max_score = score
         #   question_name += item

    # return max_score


def test_functions():
        assert bleu_implementation(["how are you heh?", "what should i eat?"], "bread is my pot") == 3.237552826118531e-78






