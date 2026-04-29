import tkinter as tk
from tkinter import messagebox, ttk
import random

# ---------- Quiz Data ----------
quiz_data = [
    {"question": "Capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
    {"question": "AI language?", "options": ["Python", "HTML", "CSS", "Java"], "answer": "Python"},
    {"question": "2 + 2 * 2 = ?", "options": ["6", "8", "4", "10"], "answer": "6"},
    {"question": "Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "Python creator?", "options": ["Elon Musk", "Bill Gates", "Guido van Rossum", "Mark Zuckerberg"], "answer": "Guido van Rossum"}
]

# ---------- Variables ----------
TIME_PER_QUESTION = 10
q_index = 0
score = 0
time_left = TIME_PER_QUESTION

# ---------- Functions ----------
def load_question():
    global time_left
    if q_index < len(quiz_data):
        q = quiz_data[q_index]
        question_label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            options[i].config(text=option, value=option)

        selected_option.set("")
        time_left = TIME_PER_QUESTION
        update_timer()
        update_progress()
    else:
        show_result()

def next_question():
    global q_index, score
    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Select an option!")
        return

    if selected_option.get() == quiz_data[q_index]["answer"]:
        score += 1

    q_index += 1
    load_question()

def update_timer():
    global time_left
    timer_label.config(text=f"Time Left: {time_left}s")

    if time_left > 0:
        time_left -= 1
        root.after(1000, update_timer)
    else:
        next_auto()

def next_auto():
    global q_index
    q_index += 1
    load_question()

def update_progress():
    progress["value"] = (q_index / len(quiz_data)) * 100

def show_result():
    result = f"Score: {score}/{len(quiz_data)}\n"
    if score == len(quiz_data):
        result += "Excellent!"
    elif score >= 3:
        result += "Good Job!"
    else:
        result += "Try Again!"

    messagebox.showinfo("Result", result)

def restart_quiz():
    global q_index, score
    q_index = 0
    score = 0
    random.shuffle(quiz_data)
    load_question()

# ---------- GUI ----------
root = tk.Tk()
root.title("Quiz App Advanced")
root.geometry("500x400")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(root, text="Quiz Game", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Timer
timer_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e2f", fg="yellow")
timer_label.pack()

# Progress Bar
progress = ttk.Progressbar(root, length=300, mode="determinate")
progress.pack(pady=10)

# Question
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, bg="#1e1e2f", fg="white")
question_label.pack(pady=20)

# Options
selected_option = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value="",
                        font=("Arial", 12), bg="#2e2e3e", fg="white",
                        selectcolor="#444")
    rb.pack(anchor="w", padx=50, pady=2)
    options.append(rb)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

next_btn = tk.Button(btn_frame, text="Next", command=next_question,
                     bg="#4CAF50", fg="white", width=10)
next_btn.grid(row=0, column=0, padx=10)

restart_btn = tk.Button(btn_frame, text="Restart", command=restart_quiz,
                        bg="#f39c12", fg="white", width=10)
restart_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.quit,
                     bg="#e74c3c", fg="white", width=10)
exit_btn.grid(row=0, column=2, padx=10)

# ---------- Start ----------
random.shuffle(quiz_data)
load_question()
root.mainloop()