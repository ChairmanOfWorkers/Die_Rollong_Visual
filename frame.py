from tkinter import *
from tkinter import ttk

from die import Die
from die_visual import create_hist

"""this func creates a hist through TKinter """
def hist_window():
	number_of_sides = dns_entry.get()
	number_of_rolls = nr_entry.get()
	file_name = fn_entry.get()
	die = Die()
	create_hist(die, number_of_sides, number_of_rolls, file_name)
	lbl_result['text'] = f'Diagram created successfully'

window = Tk()
window.title("Die Rolling Visualizer")
window.resizable(width=False, height=False)

"""Entries for the window"""
frm_entry = ttk.Frame(master=window)
#die number of sides
dns_temp = ttk.Label(master=frm_entry, text='Enter Num of Die sides')
dns_entry = ttk.Entry(master=frm_entry)
#number of rolls
nr_temp = ttk.Label(master=frm_entry, text='Number of rolls')
nr_entry = ttk.Entry(master=frm_entry)
#name of the file
fn_temp = ttk.Label(master=frm_entry, text='Name of the file')
fn_entry = ttk.Entry(master=frm_entry)

#placing fields
dns_temp.grid(row=1, column=1)
dns_entry.grid(row=1, column=2)
nr_temp.grid(row=2, column=1)
nr_entry.grid(row=2, column=2)
fn_temp.grid(row=3, column=1)
fn_entry.grid(row=3, column=2)

"""making a button"""
btn_submit = ttk.Button(master=window, text='Submit', command=hist_window)
lbl_result = ttk.Label(master=window, text="")

#placing fields №2
frm_entry.grid(row=0, column=0, padx=10)
btn_submit.grid(row=3, column=3, pady=5)
lbl_result.grid(row=3, column=0, padx=5)

window.mainloop()