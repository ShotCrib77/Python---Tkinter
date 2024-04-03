from readList import read_list
def log_answers(question_number: int, is_answer_correct: bool) -> None:
  AMOUNT_OF_QUESTIONS = 10
  
  answer_list = read_list("answers.txt")
  
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
  
  
  new_answers = ""
  for i in range(0, AMOUNT_OF_QUESTIONS):
    for item in answer_list[i]:
      new_answers += item + "\n"
    new_answers += "\n"
  
  print(new_answers)
  
  with open("answers.txt", "w", encoding="utf-8") as answers:
    answers.write(new_answers)

log_answers(0, True)