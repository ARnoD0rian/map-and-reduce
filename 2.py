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
        grades = list()
        for j in range(random.randint(5, 15)):
            grades.append(random.randint(100, 1000))
        students.append({"name": name_random, "expenses": grades})
    return students

students = generation(10)
filter_name = list()
def help_filter(x):
    global using_name
    if x["name"] in filter_name:
        return True
    return False

def my_filter():
    global students
    for key, value in my_checkbutton.items():
        if (value.get()): filter_name.append(key)
    students = list(filter(help_filter, students))
    showinfo(message="ok")
    
def help_calculate(student):
    student["sum"] = sum(student["expenses"])
    return student

def calculate_average_score():
    global students
    students = list(map(help_calculate, students))
    all_grades = ttk.Frame(root, style="Style.TFrame")
    all_grades.pack()
    all_grades_label = list()
    top = ttk.Label(all_grades, style="TLabel", text="сумма расходов людей")
    top.pack()
    for student in students:
        all_grades_label.append(ttk.Label(all_grades, style="TLabel", text=str(student["name"][:-1])+ ' ' + str(student["sum"])))
        all_grades_label[-1].pack()
    showinfo(message="ok")
            
def agregation():
    the_best = ttk.Frame(root, style="Style.TFrame")
    the_best.pack()
    sum_this = 0
    for i in range(len(students)):
        sum_this += students[i]["sum"]
    max_element = ttk.Label(the_best, style="TLabel", text=f"общая сумма {sum_this}")
    max_element.pack()
    showinfo(message="ok")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("second")
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
    style_label.configure("TLabel", font=my_font, padding=0, foreground="white", background="gray")
    style_Entry = ttk.Style()
    style_Entry.configure("TEntry", padding=5, font=my_font, foreground="black", background="gray")
    
    main_menu = tk.Menu()
    main_menu.add_cascade(label="фильтр", command=my_filter)
    main_menu.add_cascade(label="вычислить сумму расходов людей", command=calculate_average_score)
    main_menu.add_cascade(label="вычислить общую сумму", command=agregation)
    
    for_filter = ttk.Frame(root, style="Style.TFrame")
    for_filter.pack()
    tyle_frame = ttk.Style()

    using_name = list()
    for i in range(len(students)):
        using_name.append(students[i]["name"])
    my_checkbutton = dict_generation_checkbutton(using_name)
    this_checkbutton = dict()
    for line in using_name:
        this_checkbutton[line] = ttk.Checkbutton(for_filter, text=line, style="TCheckbutton", variable=my_checkbutton[line])
        this_checkbutton[line].grid(sticky="w")
        
    root.config(menu=main_menu)
    root.mainloop()