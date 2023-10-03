import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def update_task():
    selected_task = task_listbox.get(task_listbox.curselection())
    new_task_text = task_field.get()
    if selected_task and new_task_text:
        tasks.remove(selected_task)
        tasks.append(new_task_text)
        list_update()
        the_cursor.execute('update tasks set title = ? where title = ?', (new_task_text, selected_task))
        task_field.delete(0, 'end')
    else:
        messagebox.showinfo('Error', 'Select a task to update and provide a new task text.')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        while(len(tasks) != 0):
            tasks.pop()
        the_cursor.execute('delete from tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    while(len(tasks) != 0):
        tasks.pop()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Made By Eraj Hassan Khan")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(True, True)  # Added maximize button
    guiWindow.configure(bg="#87CEEB")  # Changed background color to light blue

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#87CEEB")
    functions_frame = tk.Frame(guiWindow, bg="#87CEEB")
    listbox_frame = tk.Frame(guiWindow, bg="#87CEEB")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Arial", 30),
        background="#87CEEB",
        foreground="#000000"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Times New Roman", 11, "bold"),
        background="#87CEEB",
        foreground="#000000"
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Arial", 12),
        width=18,
        background="#FFD700", 
        foreground="#000000"
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    update_button = ttk.Button(
        functions_frame,
        text="Update Task",
        width=24,
        command=update_task
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )

    add_button.configure(style='Accent.TButton')
    update_button.configure(style='Accent.TButton')
    del_button.configure(style='Accent.TButton')
    del_all_button.configure(style='Accent.TButton')
    exit_button.configure(style='Danger.TButton')

    add_button.place(x=30, y=120)
    update_button.place(x=30, y=160)
    del_button.place(x=30, y=200)
    del_all_button.place(x=30, y=240)
    exit_button.place(x=30, y=280)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        foreground="#000000",
        selectbackground="#CD853F",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
