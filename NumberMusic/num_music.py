import tkinter as tk
from tkinter import messagebox
from tkinter.constants import *

import deg_seq_to_midi as dstm

mw = None

def main_window():
	root = tk.Tk()

	tk.Label(root,text="Number Music",font=("Courier",44)).grid(row=0,column=0)

	tk.Label(root,text="Project Name",font=("Courier",20)).grid(row=3,column=0)
	project_name_field =tk.Entry(root,font=("Courier",20))
	project_name_field.grid(row=3,column=1)

	tk.Label(root,text="Major Key Root Note",font=("Courier",20)).grid(row=6,column=0)
	root_note_field =tk.Entry(root,font=("Courier",20))
	root_note_field.grid(row=6,column=1)

	tk.Label(root,text="Degrees\' Sequence",font=("Courier",34)).grid(row=10,column=0)
	deg_seq_field =tk.Entry(root,font=("Courier",20), width = 75)
	deg_seq_field.grid(row=12,column=0,columnspan=2)

	tk.Button(root,text="Save",font=("Courier",20), command = on_save_clicked ).grid(row=15,column=0)
	tk.Button(root,text="New",font=("Courier",20), command = on_new_clicked ).grid(row=15,column=1)




	return (root, project_name_field, root_note_field, deg_seq_field)


def on_save_clicked():
	global mw
	project_name = str(mw[1].get())
	arr = str(mw[3].get())
	arr = arr.split(" ")
	arr = [int(a) for a in arr]
	key_name = str(mw[2].get())
	dstm.generate(project_name,arr,key_name)
	messagebox.showinfo("Created!","Your file was successfully created")

def on_new_clicked():
	global mw
	mw[0].destroy()
	mw = main_window()



mw = main_window()
tk.mainloop()