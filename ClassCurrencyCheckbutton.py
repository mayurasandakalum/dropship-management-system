from tkinter import *
from tkinter import ttk

currency = "USD"

class currencyCheckbuttonClass(ttk.Checkbutton):
    def currencyCheckbutton(self, master, labelX, labelY, firstLabel):

        # Create variables
        self.master = master
        self.labelX = labelX
        self.labelY = labelY
        self.firstLabel = firstLabel

        # Create a variable for currencyCheckbutton
        self.currencyVar = IntVar()
        # Set it to 1
        self.currencyVar.set(1)

        # Config details to the Check button
        self.config(var=self.currencyVar)
        self.config(command=self.labeling)
        self.config(style="currencySwitch")

        # Create a blank label
        self.currencyLabel = Label()

    # Function for the process
    def labeling(self):

        # Destroy the first label
        self.firstLabel.destroy()

        # Change label to "USD"
        if self.currencyVar.get() == 1:
            currency = "USD"
        # Change label to "LKR"
        elif self.currencyVar.get() == 0:
            currency = "LKR"

        # Destroy current label
        self.currencyLabel.destroy()
        # Grid new label
        self.currencyLabel = Label(self.master, text=currency, font=('Typo Round Edited', 11), bg='#262626')
        self.currencyLabel.place(x=self.labelX, y=self.labelY)