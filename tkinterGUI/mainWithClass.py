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
        # start mainloop
        self.root.mainloop()




win = MyGUI()