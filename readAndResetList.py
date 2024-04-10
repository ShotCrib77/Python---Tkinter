AMOUNT_OF_QUESTIONS = 10
def read_list(filename: str) -> list[str]:
  with open(filename, "r", encoding="utf-8") as file:
    list_sheet = [line.strip() for line in file]
    
    file_list = [] #En lista med sublists
    temp = []
    for item in list_sheet:
      if item != "":
        temp.append(item)
      else:
        file_list.append(temp)
        temp = []
        
    file_list.append(temp)
      
  return file_list

def reset_personal_answers():
  reset_string = "\n\n".join(f"Question {i+1}:\nCorrect: 0\nIncorrect: 0" for i in range(AMOUNT_OF_QUESTIONS))
  with open("personalAnswers.txt", "w", encoding="utf-8") as filereset:
      filereset.write(reset_string)
