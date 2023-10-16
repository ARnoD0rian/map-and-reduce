import os
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
import pandas as pd
import random

def dict_generation_checkbutton(array_name)->dict:
    this_dict = dict()
    for line in array_name:
        this_dict[str(line)] = tk.IntVar()
    return this_dict

def generation(n)->list:
    students = list()
    file = open("name.txt", "r", encoding="utf-8")
    name = list()
    for line in file:
        name.append(line)
    for i in range(n):
        name_random = name[random.randint(0, len(name) - 1)]
        age = random.randint(18, 23)
        grades = list()
        for j in range(random.randint(5, 15)):
            grades.append(random.randint(1, 100))
        students.append({"name": name_random, "age": age, "grades": grades})
    return students

students = generation(50)

atribute_filter = list()
def help_filter(x):
    global atribute_filter
    if x["age"] in atribute_filter:
        return True
    return False

def my_filter():
    global students, atribute_filter
    atribute_filter = []
    for x in range(18, 24):
        if my_checkbutton[str(x)].get():
            atribute_filter.append(x)
    students = list(filter(help_filter, students))
    showinfo(message="ok")
    
def help_calculate(student):
    student["average"] = round(sum(student["grades"]) / len(student["grades"]), 1)
    return student

def calculate_average_score():
    global students
    students = list(map(help_calculate, students))
    all_grades = ttk.Frame(root, style="Style.TFrame")
    all_grades.pack()
    all_grades_label = list()
    top = ttk.Label(all_grades, style="TLabel", text="средний балл студентов")
    top.pack()
    for student in students:
        all_grades_label.append(ttk.Label(all_grades, style="TLabel", text=str(student["name"][:-1])+ ' ' + str(student["average"])))
        all_grades_label[-1].pack()
    sr_bal = 0
    for i in range(len(students)):
        sr_bal += students[i]["sum"]
    sr_bal = round(sr_bal / len(students), 1)
    sr_balls = ttk.Label(all_grades, style="TLabel", text=str("средний балл:" + sr_bal))
    sr_balls.pack()
    showinfo(message="ok")
        
def agregation():
    the_best = ttk.Frame(root, style="Style.TFrame")
    the_best.pack()
    this_write = max(students, key= lambda x: x["average"])
    name_this = this_write["name"]
    average_this = this_write["average"]
    max_element = ttk.Label(the_best, style="TLabel", text=f"самый умный студент {name_this[:-1]}: {average_this}")
    max_element.pack()
    showinfo(message="ok")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("first")
    root.geometry('600x800')
    root['background'] = "gray"
    root.resizable(True, True)
    imgicon = tk.PhotoImage(file=os.path.join('C:\home screen\programming\python\study on python\study\dataset\data\icon.ico'))
    root.tk.call('wm', 'iconphoto', root._w, imgicon) 
    
    my_font = ("Arial", 12) 
    
    style_frame = ttk.Style()
    style_frame.configure("CustomFrame.TFrame", background="white")
    style_way_frame = ttk.Style()
    style_way_frame.configure("Style.TFrame", background="gray")
    style_check_button = ttk.Style()
    style_check_button.configure("TCheckbutton", font=my_font, background="gray", foreground="white")
    style_button = ttk.Style()
    style_button.configure("TButton", font=my_font)
    style_label = ttk.Style()
    style_label.configure("TLabel", font=my_font, padding=10, foreground="white", background="gray")
    style_Entry = ttk.Style()
    style_Entry.configure("TEntry", padding=5, font=my_font, foreground="black", background="gray")
    
    main_menu = tk.Menu()
    main_menu.add_cascade(label="фильтр", command=my_filter)
    main_menu.add_cascade(label="вычислить средний балл", command=calculate_average_score)
    main_menu.add_cascade(label="найти с самым высоким средним баллом", command=agregation)
    
    for_filter = ttk.Frame(root, style="Style.TFrame")
    for_filter.pack()
    tyle_frame = ttk.Style()

    my_checkbutton = dict_generation_checkbutton([x for x in range(18, 24)])
    this_checkbutton = dict()
    for x in range(18, 24):
        this_checkbutton[str(x)] = ttk.Checkbutton(for_filter, text=str(x), style="TCheckbutton", variable=my_checkbutton[str(x)])
        this_checkbutton[str(x)].grid(sticky="w")
        
    root.config(menu=main_menu)
    root.mainloop()