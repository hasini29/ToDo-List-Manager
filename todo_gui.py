import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "tasks.txt"

# Load tasks from file
tasks = []
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        for line in file:
            task, done = line.strip().split("|")
            tasks.append({"task": task, "done": done == "True"})

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(f"{t['task']}|{t['done']}\n")

# Add task
def add_task():
    task_text = entry_task.get()
    if task_text == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append({"task": task_text, "done": False})
    listbox_tasks.insert(tk.END, f"{task_text} [❌]")
    entry_task.delete(0, tk.END)
    save_tasks()

# Mark task as done
def mark_done():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = selected[0]
    tasks[index]["done"] = True
    update_listbox()
    save_tasks()

# Delete task
def delete_task():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task!")
        return
    index = selected[0]
    tasks.pop(index)
    update_listbox()
    save_tasks()

# Update listbox
def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "❌"
        listbox_tasks.insert(tk.END, f"{t['task']} [{status}]")

# GUI Setup
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox_tasks = tk.Listbox(frame, width=40, height=10)
listbox_tasks.pack(side=tk.LEFT, padx=5)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", width=12, command=add_task)
btn_add.pack(pady=2)

btn_done = tk.Button(root, text="Mark as Done", width=12, command=mark_done)
btn_done.pack(pady=2)

btn_delete = tk.Button(root, text="Delete Task", width=12, command=delete_task)
btn_delete.pack(pady=2)

update_listbox()
root.mainloop()
