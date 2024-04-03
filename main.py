from logingFunction import log_answers
import tkinter as tk
from readList import read_list
import time

AMOUNT_OF_QUESTIONS = 10

def set_user_input(alternative_input: str):
    global user_input
    user_input = alternative_input
    print(user_input) # Debugging

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def on_closing():
    root.destroy()
    
def check_answer():
    global user_input, correct_answer, question_number
    if user_input is not None:
        if user_input == correct_answer:
            log_answers(question_number, True)
        else:
            log_answers(question_number, False)
            
        question_number += 1
        if question_number != AMOUNT_OF_QUESTIONS:
            clear_screen()
            ask_question(question_number)
        else:
            pass
            #show stats 
        
def ask_question(i):
    print(i)
    top = tk.Frame(root)
    top.pack(expand=True, fill="both")
    alternatives = tk.Frame(root)
    alternatives.pack(expand=True, fill='both')
    button_container = tk.Frame(root)
    button_container.pack(expand=True, fill='both')
    button_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    global user_input, correct_answer
    user_input = None
    question = question_list[i][0]
    alternative_1 = question_list[i][1]
    alternative_x = question_list[i][2]
    alternative_2 = question_list[i][3]
    correct_answer = question_list[i][4]
    
    question_text = (f"Fråga {str(i+1)}: {question}")
    alternative_1_lable = (f"1. {alternative_1}")
    alternative_x_lable = (f"X. {alternative_x}")
    alternative_2_lable = (f"2. {alternative_2}")
    
    header = tk.Label(top, text = "Tipspromenad!", font=("Arial", 16))
    header.pack(pady=16)
    question_lable = tk.Label(top, text = question_text, font=("Arial", 12))
    question_lable.pack()
    
    alternative_1_lable = tk.Label(top, text = alternative_1_lable, font=("Arial", 10))
    alternative_1_lable.pack(side="top", pady=5)
    
    alternative_x_lable = tk.Label(top, text = alternative_x_lable, font=("Arial", 10))
    alternative_x_lable.pack(side="top", pady=5)
    
    alternative_2_lable = tk.Label(top, text = alternative_2_lable, font=("Arial", 10))
    alternative_2_lable.pack(side="top", pady=5)
        
    button_1 = tk.Button(button_container, text="1", command=lambda: set_user_input("1"))
    button_1.pack(side='left', padx=5)

    button_x = tk.Button(button_container, text="X", command=lambda: set_user_input("X"))
    button_x.pack(side='left', padx=5)

    button_2 = tk.Button(button_container, text="2", command=lambda: set_user_input("2"))
    button_2.pack(side='left', padx=5)
    
    next_question_button = tk.Button(root, text="Next Question", command=check_answer)
    next_question_button.pack(pady=10)
    
    root.update()


root = tk.Tk()
root.title("Tipspromenad")
root.geometry("550x400") 
root.protocol("WM_DELETE_WINDOW", on_closing)

question_list = read_list("questions.txt")

question_number = 0
ask_question(question_number)

root.mainloop()