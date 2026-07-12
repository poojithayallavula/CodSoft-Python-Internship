from tkinter import *
from tkinter import messagebox

# Counters
total_tasks = 0
completed_tasks = 0
deleted_tasks = 0

# Update Statistics
def update_stats():
    pending_tasks = total_tasks - completed_tasks - deleted_tasks

    total_label.config(text=f"Total Tasks: {total_tasks}")
    completed_label.config(text=f"Completed: {completed_tasks}")
    pending_label.config(text=f"Pending: {pending_tasks}")
    deleted_label.config(text=f"Deleted: {deleted_tasks}")

# Add Task
def add_task():
    global total_tasks

    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    task_listbox.insert(END, "❌ " + task)
    task_entry.delete(0, END)

    total_tasks += 1
    update_stats()

# Complete Task
def complete_task():
    global completed_tasks

    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if task.startswith("❌"):
            task = task.replace("❌", "✅", 1)

            task_listbox.delete(selected)
            task_listbox.insert(selected, task)

            completed_tasks += 1
            update_stats()

    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Delete Task
def delete_task():
    global deleted_tasks

    try:
        selected = task_listbox.curselection()[0]

        task_listbox.delete(selected)

        deleted_tasks += 1
        update_stats()

    except:
        messagebox.showwarning("Warning", "Select a task first!")

# ---------------- GUI ----------------

root = Tk()
root.title("To-Do List Dashboard")
root.geometry("600x550")
root.resizable(False, False)

title = Label(root,
              text="TO-DO LIST DASHBOARD",
              font=("Arial",18,"bold"))
title.pack(pady=10)

# Statistics
stats_frame = Frame(root)
stats_frame.pack(pady=5)

total_label = Label(stats_frame,
                    text="Total Tasks: 0",
                    font=("Arial",11,"bold"),
                    fg="blue")
total_label.grid(row=0,column=0,padx=15)

completed_label = Label(stats_frame,
                        text="Completed: 0",
                        font=("Arial",11,"bold"),
                        fg="green")
completed_label.grid(row=0,column=1,padx=15)

pending_label = Label(stats_frame,
                      text="Pending: 0",
                      font=("Arial",11,"bold"),
                      fg="orange")
pending_label.grid(row=0,column=2,padx=15)

deleted_label = Label(stats_frame,
                      text="Deleted: 0",
                      font=("Arial",11,"bold"),
                      fg="red")
deleted_label.grid(row=0,column=3,padx=15)

# Entry Box
task_entry = Entry(root,
                   width=40,
                   font=("Arial",12))
task_entry.pack(pady=15)

# Buttons
button_frame = Frame(root)
button_frame.pack()

Button(button_frame,
       text="Add Task",
       width=15,
       bg="#4CAF50",
       fg="white",
       command=add_task).grid(row=0,column=0,padx=5)

Button(button_frame,
       text="Complete Task",
       width=15,
       bg="#2196F3",
       fg="white",
       command=complete_task).grid(row=0,column=1,padx=5)

Button(button_frame,
       text="Delete Task",
       width=15,
       bg="#F44336",
       fg="white",
       command=delete_task).grid(row=0,column=2,padx=5)

# Task List
task_listbox = Listbox(root,
                       width=60,
                       height=18,
                       font=("Arial",12))

task_listbox.pack(pady=20)

update_stats()

root.mainloop()