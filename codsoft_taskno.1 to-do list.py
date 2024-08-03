import tkinter
from tkinter import messagebox, Label, TOP, filedialog
import pickle

win = tkinter.Tk()
win.title("To-Do List")
win.config(background='light gray')

winlabel = tkinter.Label(win, text="To-Do List", bg='white', font=("Times", 18, 'bold'))
winlabel.pack(side=tkinter.TOP, pady=5)

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(0, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def markcompleted():
    try:
        marked = listbox_tasks.curselection()
        if not marked:
            tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")
            return
        temp_index = marked[0]
        temp_marked = listbox_tasks.get(temp_index)
        temp_marked = temp_marked + " ✔"
        listbox_tasks.delete(temp_index)
        listbox_tasks.insert(temp_index, temp_marked)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def exit_window():
    win.destroy()

# Widgets

#FRAME TO HOLD LISTBOX AND SCROLLBAR
frame_tasks = tkinter.Frame(win)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=8, width=55, bg='#a6a6a6', font=15)
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.BOTH, pady=10)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)



#input
entry_task = tkinter.Entry(win, bg='light yellow', font=15)
entry_task.pack(ipadx=30, ipady=4, pady=10)

#buttons
button_add_task = tkinter.Button(win, text='Add Task', bg='#c5f776', width=20, command=add_task, pady=2)
button_add_task.pack(pady=2)

button_delete_task = tkinter.Button(win, text='Delete selected task', bg='light pink', width=20, command=delete_task, pady=2)
button_delete_task.pack(pady=2)

mark_button = tkinter.Button(win, text="Mark as completed",bg='light blue', width=20, command=markcompleted)
mark_button.pack(pady=3)

exit_button = tkinter.Button(win, text="Exit", bg='red', width=20, command=exit_window)
exit_button.pack(pady=3)

win.mainloop()