import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()

widgets_frame = Frame(root)
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
#widgets_frame.columnconfigure(index=0, weight=1)



# Create a style
style = ttk.Style(widgets_frame)

# Import the tcl file
root.tk.call("source", "D:/Documents/My Documents/Ebay & Paypal 1/DropShip Managemet System/GUI Icon Checking/dark.tcl")

# Set the theme with the theme_use method
style.theme_use("azure-dark")

### Class for entry boxes
class entry_box:
    def __init__(self, frame, row, padx, var='', entry_height=0):
        
        # Define Variables
        self.var_i = IntVar()
        self.common_var = StringVar()

        self.frame = frame
        self.row = row
        self.entry_height = entry_height
        self.padx = padx
        
        if var == '':
            self.var = self.common_var
        else:
            self.var = var
        

        # Create Entry Box
        self.entry = ttk.Entry(self.frame, background='white', textvariable=self.var, state='normal', style="Entryx")
        self.entry.grid(row=self.row, column=3, padx=(self.padx,0), pady=(0,10), ipady=self.entry_height, sticky=E)



class checkbox_with_entry(entry_box):

    def __init__(self, frame, row, padx, entry_state='n', var='', entry_height=0, check='N'):
        super().__init__(frame, row, padx, var=var, entry_height=entry_height)
        self.entry_state = entry_state
        self.check = check

        self.decide_check_process()


    # Decide checkbox want or not
    def decide_check_process(self):
        if self.check == "Y":
            self.var_i.set(1)
            self.check_process()

        # In beginnig disable entry box for 'data added date' entry box
        if self.entry_state == "d":
            self.entry.configure(state='disabled')
        else:
            pass

    # If want checkbox create it
    def check_process(self):
        self.check = ttk.Checkbutton(self.frame, text='Disable', variable=self.var_i, command=self.decide_check_with_entry_state, style="Switch")
        self.check.grid(row=self.row, column=2, padx=(5,0), pady=(0,10))

    # Select whether the state of the entry box should change when the checkbox is working.
    def decide_check_with_entry_state(self):
        if self.entry_state == 'd':
            self.check_with_entry_state()
        else:
            pass
    # If want it create there process
    def check_with_entry_state(self):
        if self.var_i.get() == 1:
            self.entry.configure(state='disabled')
        else:
            self.entry.configure(state='normal')

from datetime import date

ebay_data_added_date_sl_var = StringVar()

today_date = date.today()
ebay_data_added_date_sl_var.set(today_date)


ebay_data_added_date_sl_text_box = checkbox_with_entry(frame=root, row=1, padx=10, var=ebay_data_added_date_sl_var, entry_state="d", check='Y')


"""switch = ttk.Checkbutton(widgets_frame, text="Switch", style="Switch")
switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")
"""
# Start the main loop
root.mainloop()
