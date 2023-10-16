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
    name = [str(x) for x in range(101, 111)]
    for i in range(n):
        customer_id = random.randint(101, 110)
        students.append({"order_id": str(i + 1), "customer_id": str(customer_id), "amount": random.randint(50, 1000)})
    return students

students = generation(50)
filter_name = list()
def help_filter(x):
    global using_name
    if x["customer_id"] in filter_name:
        return True
    return False

def my_filter():
    global students
    for key, value in my_checkbutton.items():
        if (value.get()): filter_name.append(key)
    students = list(filter(help_filter, students))
    showinfo(message="ok")
    
def help_calculate(student):
    global students
    student["sum"] = 0
    student["len"] = 0
    for i in range(len(students)):
        if student["customer_id"] == students[i]["customer_id"]:
            student["sum"] += students[i]['amount']
            student["len"] += 1
    return student

def calculate_average_score():
    global students
    students = list(map(help_calculate, students))
    i = 0
    while i < len(students):
        j = i + 1
        while j < len(students):
            if students[i]["customer_id"] == students[j]["customer_id"]:
                students.pop(j)
            else:
                j += 1
        i += 1
    students.sort(key= lambda x: x["customer_id"])
    all_grades = ttk.Frame(root, style="Style.TFrame")
    all_grades.pack()
    all_grades_label = list()
    top = ttk.Label(all_grades, style="TLabel", text="сумма заказов людей")
    top.pack()
    for student in students:
        all_grades_label.append(ttk.Label(all_grades, style="TLabel", text=str(student["customer_id"])+ ":" + str(student["sum"])))
        all_grades_label[-1].pack()
    showinfo(message="ok")
        
def agregation():
    the_best = ttk.Frame(root, style="Style.TFrame")
    the_best.pack()
    sum_this = 0
    for i in range(len(students)):
        students[i]["average"] = round(students[i]["sum"] /  students[i]["len"], 1)
    for i in range(len(students)):
        average_this = students[i]["average"]
        id_this = students[i]["customer_id"]
        max_element = ttk.Label(the_best, style="TLabel", text=f"средняя цена заказов {id_this}: {average_this}")
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
    main_menu.add_cascade(label="подсчитать сумму заказов", command=calculate_average_score)
    main_menu.add_cascade(label="подсчитать среднюю стоимость заказов", command=agregation)
    
    for_filter = ttk.Frame(root, style="Style.TFrame")
    for_filter.pack()
    tyle_frame = ttk.Style()

    using_name = set()
    for i in range(len(students)):
        using_name.add(str(students[i]["customer_id"]))
    using_name = list(using_name)
    using_name.sort()
    my_checkbutton = dict_generation_checkbutton(using_name)
    this_checkbutton = dict()
    for line in using_name:
        this_checkbutton[line] = ttk.Checkbutton(for_filter, text=line, style="TCheckbutton", variable=my_checkbutton[line])
        this_checkbutton[line].grid(sticky="w")
        
    root.config(menu=main_menu)
    root.mainloop()