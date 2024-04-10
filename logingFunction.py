from readAndResetList import read_list
AMOUNT_OF_QUESTIONS = 10
def log_answers(filename: str, question_number: int, is_answer_correct: bool) -> None:
  
  answer_list = read_list(filename)
  
  if is_answer_correct:
    correct_answers = answer_list[question_number][1].split(" ")
    correct_answers_value = str(int(correct_answers[1]) + 1)
    new_correct_answers = correct_answers[0] + " " + correct_answers_value
    
    answer_list[question_number].pop(1)
    answer_list[question_number].insert(1, new_correct_answers)
    
  else:
    incorrect_answers = answer_list[question_number][2].split(" ")
    incorrect_answers_value = str(int(incorrect_answers[1]) + 1)
    new_incorrect_answers = incorrect_answers[0] + " " + incorrect_answers_value
    
    answer_list[question_number].pop(2)
    answer_list[question_number].insert(2, new_incorrect_answers)
  
  new_answers = '\n\n'.join('\n'.join(sublist) for sublist in answer_list)
  with open(filename, "w", encoding="utf-8") as answers:
    answers.write(new_answers)