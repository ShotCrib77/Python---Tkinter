
with open("questons.txt", "r", encoding="utf-8") as questions:
    question_sheet = [line.strip() for line in questions]
    
    question_list = [] #En lista med sublist (för varje fråga+svar där [0] = Fårgan)
    temp = []
    for item in question_sheet:
        if item != "":
            temp.append(item)
        else:
            if temp:
                question_list.append(temp)
                temp = []

for i in range(0,9):
    question = question_list[i][0]
    answer_1 = question_list[i][1]
    answer_x = question_list[i][2]
    answer_2 = question_list[i][3]

    print(question)
    print("1. " + answer_1)
    print("X. " + answer_x)
    print("2. " + answer_2)
    
    user_input = input().upper()
    

def log_answers():
    with open("answers.txt" "r+", encoding="utf-8"):
        pass