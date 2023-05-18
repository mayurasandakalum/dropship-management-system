#from classes3 import testfun
from tkinter import *
from tkinter import ttk
import tkinter as tk
import datetime
from PIL import ImageTk,Image

from pynput.keyboard import Key, Controller

keyboard = Controller()

### Class for entry boxes
class entry_box:
    def __init__(self, frame, row, padx=0, var='', entry_height=0, entryStyle="EntryLong1", entry_width=5, sticky=E):
        
        # Define Variables
        self.var_i = IntVar()
        self.common_var = StringVar()

        self.frame = frame
        self.row = row
        self.entry_height = entry_height
        self.entry_width = entry_width
        self.padx = padx
        self.sticky = sticky
        
        if var == '':
            self.var = self.common_var
        else:
            self.var = var

        # Create Entry Box
        self.entry = ttk.Entry(self.frame, background='white', textvariable=self.var, state='normal',font=('Nova Round', 11) ,style=entryStyle, width=self.entry_width)
        self.entry.grid(row=self.row, column=1, padx=(self.padx,0), pady=(0,20), ipady=self.entry_height, sticky=self.sticky)
        
class checkbox_with_entry(entry_box):

    def __init__(self, frame, row, padx, entryStyle="EntryLong1", entry_state='n', var='', entry_height=0, check='N', sticky=E):
        super().__init__(frame, row, padx, var=var, entry_height=entry_height, entryStyle=entryStyle, sticky=sticky)
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
        self.check = ttk.Checkbutton(self.frame, variable=self.var_i, command=self.decide_check_with_entry_state, style="lockSwitch")
        self.check.grid(row=self.row-1, column=1, pady=(0,10))

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

### Label Class
class label_class:
    def __init__(self, master_frame, rowNum, txt, padx=40):
        self.label = Label(master_frame, text=txt, font = ("Typo Round Bold Demo", 11), justify=LEFT, bg='#1f1f1f', fg='#626262') #font=('Gelion Black', 18)
        self.label.grid(row=rowNum, column=1, padx=(padx,0), pady=(0,10), sticky="W")

### Class for sub frames

class Subframe:
    def __init__(self, master_frame, row, text, column=1, ipady=0, padyUp=10):
        self.master_frame = master_frame
        self.row = row
        self.column = column
        self.text = text
        self.ipady = ipady
        self.padyUp = padyUp

        # Frame Title
        self.title = Label(self.master_frame, text=self.text, font=('Typo Round Bold Demo', 16),fg="White", bg='#1f1f1f')
        self.title.grid(row = self.row - 1, column = 1, pady = (self.padyUp,20), padx = 30, sticky=W)

        # Create a sub frame
        self.frame = Frame(self.master_frame, bg='#1f1f1f')
        self.frame.grid(row = self.row, column = self.column, padx = 5, sticky = W, ipadx=80, ipady=self.ipady)


### Class for Scrolled Window / Frame / Canvas with Mousewheel

# Import Libraries
import functools
fp = functools.partial
from sys import platform

# Create it...
class VerticalScrolledFrame(ttk.Frame):
    """
    A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    * This comes from a different naming of the the scrollwheel 'button', on different systems.
    """
    def __init__(self, parent, *args, **kw):

        super().__init__(parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        self.vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        self.canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(self.canvas)
        self.interior_id = self.canvas.create_window(0, 0, window=self.interior, anchor=NW)

        self.interior.bind('<Configure>', self._configure_interior)
        self.canvas.bind('<Configure>', self._configure_canvas)
        self.canvas.bind('<Enter>', self._bind_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbind_from_mousewheel)
        
        
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar

    def _configure_interior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)

        '''if self.interior.winfo_reqwidth() != self.winfo_width():
            # update the canvas's width to fit the inner frame'''
        self.canvas.config(width=455)

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(self.interior_id, width=self.winfo_width())

    # This can now handle either windows or linux platforms
    def _on_mousewheel(self, event, scroll=None):

        if platform == "linux" or platform == "linux2":
            self.canvas.yview_scroll(int(scroll), "units")
        else:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _bind_to_mousewheel(self, event):
        if platform == "linux" or platform == "linux2":
            self.canvas.bind_all("<MouseWheel>", fp(self._on_mousewheel, scroll=-1))
            self.canvas.bind_all("<Button-5>", fp(self._on_mousewheel, scroll=1))
        else:
            self.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_from_mousewheel(self, event):

        if platform == "linux" or platform == "linux2":
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.unbind_all("<MouseWheel>")

### Create class for 'Paid_date' entry box process
class paid_date_entry_box(entry_box): # Child class of entry_box class
    # Create months' short names list
    global months_list
    months_list = [('JAN',31), ('FEB',29), ('MAR',31), ('APR',30), ('MAY',31), ('JUN',30), ('JUL',31), ('AUG',31), ('SEP',30), ('OCT',31), ('NOV',30), ('DEC',31)]
    
    def __init__(self, frame, row, padx, var='', entry_height=0):
        # import init method from entry_box class which is parent class
        super().__init__(frame, row, padx, var=var, entry_height=entry_height)

        # Call to the function
        self.paid_date_process()
    
    def paid_date_process(self):
        # Define global variables
        global symbol
        global paid_date_output_label
        paid_date_output_label = Label(self.frame)
        symbol = Label(self.frame)

        def fun(event):
            """if str(event)[1:12] == "ButtonPress":
                print('hi')"""

            nonstrip = self.var.get() # Get original text from entry box
            global striped
            striped = nonstrip.strip() # Remove all blank spaces on either side of the text.
            short = striped[:3] # Get first 3 letters to a variable (month's short name)

            # Check if it is equal to or less than 6 characters
            if len(striped) <= 6:
                # Check if the first 3 letter of the above text is the same as the item in the months_list.
                for month in months_list:
                    if short.lower() == month[0].lower():
                        month_check = "y"
                        break
                    else:
                        month_check = "n"

                # Check date's digits
                if month_check == 'y':
                    if len(striped[4:]) == 2:
                        try:
                            int_date = int(striped[4:])
                            int_check = 'y2' # y2 = 2 digit date 'yes' 

                            if 0 < int_date and int_date <= month[1]:
                                relevent_date = str(int_date) 
                            else:
                                relevent_date = 'Please enter a correct date'
                        except Exception as e:
                            int_check = 'n'

                    elif len(striped[4:]) == 1:
                        try:
                            int_date = int(striped[4:])
                            int_check = 'y1' # y1 = 1 digit date 'yes'

                            if 0 < int_date and int_date <= month[1]:
                                relevent_date = str(int_date)
                            else:
                                relevent_date = 'Please enter a correct date'

                        except Exception as e:
                            int_check = 'n'
                            #month_error = 'n'

                    else:
                        int_check = 'n'

                    # Create month number
                    if int_check == 'y2' or int_check == 'y1':
                        month_num = months_list.index(month) + 1
                        if len(str(month_num)) == 1:
                            relevent_month = '0' + str(month_num)
                        else:
                            relevent_month = str(month_num)
                    elif int_check == 'n':
                        relevent_date = 'Please enter a correct date'
                        
                    # Define relevent year
                    relevent_year = str(datetime.datetime.now().year)
                    
                    # Lastly create date 
                    if relevent_date == 'Please enter a correct date':
                        paid_date = relevent_date
                    else:
                        if int_check == 'y2':
                            #relevent_date = str(int_date)
                            paid_date = relevent_year + ' - ' + relevent_month + ' - ' + relevent_date
                            #print(paid_date)

                        elif int_check == 'y1':
                            #relevent_date = str(int_date)
                            paid_date = relevent_year + ' - ' + relevent_month + ' - ' + '0' + relevent_date

                elif month_check == 'n':
                    paid_date = 'Please enter a correct month'

            else:
                paid_date = 'Please enter the date in the correct type'

            global paid_date_output_label
            global symbol
            if len(paid_date) == 14:
                paid_date_output_label.destroy()
                symbol.destroy()
                paid_date_output_label = Label(self.frame, text=paid_date, fg='#25aa0e', font=('Typo Round Edited', 10), bg='#1f1f1f')
                paid_date_output_label.place(x=355, y=242)
                symbol = Label(self.frame, text= u'\u2713', fg='#25aa0e', font=('Typo Round Edited', 13), justify='left', bg='#262626')
                symbol.place(x=407, y=207)
            
            else:
                paid_date_output_label.destroy()
                symbol.destroy()
                paid_date_output_label = Label(self.frame, text=paid_date, fg='red', font=('Typo Round Edited', 10), justify='left', bg='#1f1f1f')

                symbol = Label(self.frame, text= '!', fg='red', font=('aKandyNew', 16), justify='left', bg='#262626')
                symbol.place(x=410, y=206.5)
                                
                if len(paid_date) == 28:
                    paid_date_output_label.place(x=259, y=242)
                elif len(paid_date) == 27:
                    paid_date_output_label.place(x=268, y=242)
                elif len(paid_date) == 41:
                    paid_date_output_label.place(x=190, y=242)


        # Bind 'Enter Key' and 'Tab Key' with the entry box in entry_box class
        self.entry.bind('<Return>', fun)
        #self.entry.bind('<Tab>', fun)
        #self.entry.bind('<Button-1>', fun)FocusOut
        self.entry.bind('<FocusOut>', fun)


### Create class for 'listingID' entry box process
class listingID_class(entry_box):
    def __init__(self, frame, row, padx, var, entry_height=0):
        super().__init__(frame, row, padx, var=var, entry_height=entry_height)
        
        # Call function for start process
        self.listingID_process()

    def listingID_process(self):
        global listingID_out_label
        listingID_out_label = Label(self.frame)

        listingID_var = self.var

        def callback(listingID_var):
            global listingID_out_label
            listingID_out_label.destroy()
            
            nonstiped = listingID_var.get()
            stripted = nonstiped.strip()
            listingID_var.set(stripted)

            if len(stripted) < 12 and len(stripted) > 0:
                listingID_out_label = Label(self.frame, text = str(12-len(stripted)) + ' more\ncharacters needed.', justify='left', bg='white')
            elif len(stripted) > 12:
                listingID_out_label = Label(self.frame, text='Passed the\nmaximum value', fg='red', justify='left', bg='white')
                listingID_var.set(stripted[:12])
            elif len(stripted) == 12:
                listingID_out_label = Label(self.frame, text=u'\u2713', fg='green', font=('size=5'), anchor='w', bg='white')
            elif len(stripted) == 0:
                listingID_out_label = Label(self.frame, text='', bg='white')
            
            listingID_out_label.place(x=363, y = -6)

        #sv = StringVar()
        listingID_var.trace("w", lambda name, index, mode, listingID_var=listingID_var: callback(listingID_var))

### Create class for 'listing_title' entry box process
class listing_title_class(entry_box):
    def __init__(self, frame, row, padx, var, entry_height=0):
        super().__init__(frame, row, padx, var=var, entry_height=entry_height)

        # Call function for start process
        self.listing_title_process()

    def listing_title_process(self):
        global listingTitle_out_label
        listingTitle_out_label = Label(self.frame)

        listing_title_var = self.var

        def callback(listing_title_var):
            nonstiped = listing_title_var.get()
            stripted = nonstiped.strip()
            listing_title_var.set(stripted)

            global listingTitle_out_label
            listingTitle_out_label.destroy()
            if len(stripted) != 0:
                if len(stripted) < 80:
                    out = str(len(stripted)) + ' Characters'
                    listingTitle_out_label = Label(self.frame, text=out, bg='white')
                    listingTitle_out_label.place(x=364, y=35)
                elif len(stripted) == 80:
                    out = str(len(stripted)) + ' Characters\n(Max)'
                    listingTitle_out_label = Label(self.frame, text=out, fg='green', bg='white')
                    listingTitle_out_label.place(x=364, y=28)
                else:
                    out = str(len(stripted)) + ' Characters\n(Pass Maximum)'
                    listingTitle_out_label = Label(self.frame, text=out, fg='red', justify = LEFT, bg='white')
                    listingTitle_out_label.place(x=364, y=28)

        listing_title_var.trace("w", lambda name, index, mode, listing_title_var=listing_title_var: callback(listing_title_var))

# Sold Price(Without Tax) Class
class sold_price_without_tax_class(entry_box):
    def __init__(self, frame, row, padx, var, entry_height=0):
        #var.set(45454.233)
        super().__init__(frame, row, padx, var=var, entry_height=entry_height)

        # Call the method
        """self.process()
    
    def process(self):

        var = self.var
        print(var)

        def callback(var):
            global abb
            abb = var.get()
            

        var.trace("w", lambda name, index, mode, var=var: callback(var))
        return abb"""

# Canvas Shapes(Images) Class
class canvas_shape_class:
    def __init__(self,f, row, column, x, y):
        canvas = Canvas(f, width = 170, height = 144, bg='#1f1f1f', highlightthickness=0)  
        canvas.grid(row=row, column=column, padx=x, pady=y)  
        image = 'Canvas Shapes/' + str(row) + '.' + str(column) + '.png'
        a = Image.open('Canvas Shapes/' + str(row) + '.' + str(column) + '.png')
        a = a.resize((170, 140), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(a)
        canvas.create_image(85,75, image=self.img)

        """n = sold_price_without_tax_class()
        v = n.process()"""


        canvas.create_text(78,86 ,text='$99.99', fill='white', font=('Gelion Black', 21))


class AutocompleteCombobox(ttk.Combobox):

	def set_completion_list(self, completion_list, comboStyle, var=None):
		"""Use our completion list as our drop down selection menu, arrows move through menu."""
		self._completion_list = sorted(completion_list, key=str.lower) # Work with a sorted list
		self._hits = []
		self._hit_index = 0
		self.position = 0
		self.config(textvariable=var)
		self.config(style=comboStyle)
		self.config(font=('Typo Round Edited', 10))
		self.config(width=5)
		self.bind('<KeyRelease>', self.handle_keyrelease)
		self['values'] = self._completion_list  # Setup our popup menu

	def autocomplete(self, delta=0):
		"""autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
		if delta: # need to delete selection otherwise we would fix the current position
			self.delete(self.position, END)
		else: # set position to end so selection starts where textentry ended
			self.position = len(self.get())
		# collect hits
		_hits = []
		for element in self._completion_list:
			if element.lower().startswith(self.get().lower()): # Match case insensitively
				_hits.append(element)
		# if we have a new hit list, keep this in mind
		if _hits != self._hits:
			self._hit_index = 0
			self._hits=_hits
		# only allow cycling if we are in a known hit list
		if _hits == self._hits and self._hits:
			self._hit_index = (self._hit_index + delta) % len(self._hits)
		# now finally perform the auto completion
		if self._hits:
			self.delete(0,END)
			self.insert(0,self._hits[self._hit_index])
			self.select_range(self.position,END)

	def handle_keyrelease(self, event):
		#print (event.keysym)
		"""event handler for the keyrelease event on this widget"""
		if event.keysym == "BackSpace":
			self.delete(self.index(INSERT), END)
			self.position = self.index(END)
		if event.keysym == "Left":
			if self.position < self.index(END): # delete the selection
				self.delete(self.position, END)
			else:
				self.position = self.position-1 # delete one character
				self.delete(self.position, END)
		if event.keysym == "Return":
			self.position = self.index(END) # go to end (no selection)
			self.icursor(self.position)
			keyboard.press(Key.right)
				
		if len(event.keysym) == 1:
			self.autocomplete()