import tkinter as tk
from readAndResetList import read_list

AMOUNT_OF_QUESTIONS = 10
def show_stats_file(window: object, filename: str, left_or_right: str) -> None: # Visar stats från 1 fil

  show_stats_frame = tk.Frame(window)
  show_stats_frame.pack(padx = 50, side=left_or_right)
  
  stats = read_list(filename)
  row_index = 1
  for i in range(AMOUNT_OF_QUESTIONS):
    the_question_frame = tk.Frame(show_stats_frame)
    the_question_frame.grid(row=row_index, column=i % 3)
    the_question_number = stats[i][0] # variabel namnbyte..
    correct = stats[i][1]
    incorrect = stats[i][2]
    
    the_question_number_label = tk.Label(the_question_frame, text=the_question_number, font=("Arial", 14))
    the_question_number_label.pack(pady=(30, 0))
    
    correct_answers_label = tk.Label(the_question_frame, text=correct, font=("Arial", 12))
    correct_answers_label.pack(padx=20)
    incorrect_answers_label = tk.Label(the_question_frame, text=incorrect, font=("Arial", 12))
    incorrect_answers_label.pack(padx=20)
    
    if (i + 1) % 3 == 0:
      row_index += 1
def show_stats(window: object) -> None: # Visar stats från båda filerna
  
  top = tk.Frame(window)
  top.pack(pady=20)
  header = tk.Label(top, text = "Statistik!", font=("Arial", 18))
  header.pack(side="top")
  user_answers = tk.Label(top, text = "Dina svar!", font=("Arial", 16))
  user_answers.pack(side="left", padx=150)
  old_answers = tk.Label(top, text = "Andras svar!", font=("Arial", 16))
  old_answers.pack(side="right",  padx=150)
  
  show_stats_file(window, "personalAnswers.txt", "left")
  show_stats_file(window, "answers.txt", "right")
  
  window.mainloop()
