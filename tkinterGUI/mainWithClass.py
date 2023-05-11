import tkinter as tk

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

        # create an integer variable intant to hold the checkbox state
        self.checkbox_state = tk.IntVar()
        # create a checkbox
        self.checkbox = tk.Checkbutton(self.root, text="checkbox", font=("Arial", 16), variable=self.checkbox_state)
        # add checkbox to window
        self.checkbox.pack()
        
        # create button
        self.message_show_button =  tk.Button(self.root, text="show message", font=("Arial", 14))
        # add button to window
        self.message_show_button.pack()
        
        # start mainloop - MUST
        self.root.mainloop()




win = MyGUI()