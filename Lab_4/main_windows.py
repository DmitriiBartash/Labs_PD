import tkinter as tk
# import datetime
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from Lab_3_PD import * 
import os

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('500x200')

def file_clicked():
    try:
        result = find_dataset(filename_path, date_input_entry.get())
        # print(result[0],result[1])

        print (result)
        result_output = result[0].strftime("%Y-%m-%d %H:%M:%S")

        msg = f'Your date is: {result_output} on stroke {result[1]+1}'

        showinfo(
            title='Information',
            message=msg
        )
    except Exception as e:
        showinfo(title='Error', message=str(e))

# store 
date_input = tk.StringVar()

def select_file():
    global filename_path

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir= os.getcwd(),
        filetypes=filetypes)

    filename_path = filename
    
    if filename_path == "":
         showinfo(
                title='Error',
                message="You did not select the file path"
            )
    else:
        showinfo(
                title='Selected File',
                message=filename
            )

def select_folder():
    global save_path_folder

    directory_path = fd.askdirectory(
        title='Open a directory',
        initialdir= os.getcwd(),
        )
    
    save_path_folder = directory_path
    
    if save_path_folder == "":
         showinfo(
                title='Error',
                message="You did not select the folder path"
            )
    else:
        showinfo(
                title='Selected File',
                message=save_path_folder
            ) 


def append_clicked():
    made_annotations(filename_path,save_path_folder)

# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(fill='x',expand=True)

# date_input
date_input_label = ttk.Label(root, text="Date_input Address:")
date_input_label.pack(fill='x', expand=True)

date_input_entry = ttk.Entry(root, textvariable=date_input)
date_input_entry.pack(fill='x', expand=True)
date_input_entry.focus()

# Find date button
date_find_button = ttk.Button(root, text="Получить данные", command=file_clicked)
date_find_button.pack(fill='x', expand=True, pady=10)

# open button
open_button2 = ttk.Button(
    root,
    text='Open a Folder',
    command=select_folder
)
open_button2.pack(fill='x', expand=True)

# Save annotations
append_button = ttk.Button(root, text="Сохранить аннотацию", command=append_clicked)
append_button.pack(fill='x', expand=True, pady=10)

# run the application
root.mainloop()
