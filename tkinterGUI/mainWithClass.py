import tkinter as tk

class MyGUI:
    # constructor
    def __init__(self):
        # inicialize a window instant
        self.root = tk.Tk()
        # create a label(text content)
        self.label = tk.Label(self.root, text="Content", font=("Arial", 18))
        # add label to window
        self.label.pack(padx=20, pady=20)
        # create a textbox 
        self.textbox = tk.Text(self.root, height=5, font=("Arial",16))
        # add textbox to window
        self.textbox.pack(padx=10, pady=10)
        # start mainloop
        self.root.mainloop()




win = MyGUI()