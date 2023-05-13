import tkinter as tk
from tkinter import messagebox

class MyGUI:
    # constructor
    def __init__(self):
        # inicialize a window instant - MUST
        self.root = tk.Tk()
        
        # create a label(text content)
        self.label = tk.Label(self.root, text="Content", font=("Arial", 18))
        # add label to window
        self.label.pack(padx=20, pady=20)
        
        # create a textbox 
        self.textbox = tk.Text(self.root, height=5, font=("Arial",16))
        # add textbox to window
        self.textbox.pack(padx=10, pady=10)
        # bind key event to textbox
        self.textbox.bind("<KeyPress>", self.shortcut)

        # create an integer variable intant to hold the checkbox state
        self.checkbox_state = tk.IntVar()
        # create a checkbox
        self.checkbox = tk.Checkbutton(self.root, text="checkbox", font=("Arial", 16), variable=self.checkbox_state)
        # add checkbox to window
        self.checkbox.pack()
        
        # create button - on click, it calls the 'show_message' method
        self.message_show_button =  tk.Button(self.root, text="show message", font=("Arial", 14), command=self.show_message)
        # add button to window
        self.message_show_button.pack()
        
        # start mainloop - MUST
        self.root.mainloop()

    # create method for button logic
    def show_message(self):
        if self.checkbox_state.get() == 0:
            ## print textbox message, using a getter method
            print(self.textbox.get('1.0', tk.END))
        else:
            ## print a messagebox
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    ## show message when left ctrl + enter is pressed
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

win = MyGUI()