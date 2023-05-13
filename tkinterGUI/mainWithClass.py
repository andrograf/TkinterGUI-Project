import tkinter as tk
from tkinter import messagebox

class MyGUI:
    # constructor
    def __init__(self):
        # inicialize a window instant - MUST
        self.root = tk.Tk()
        
        # create menu
        self.menu_bar = tk.Menu(self.root)
        # create submenu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close With Question", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close", command=exit)

        # add submenu to menu instant
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        # add menu to window
        self.root.config(menu=self.menu_bar)

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
        # create clear button
        self.clear_text_button = tk.Button(self.root, text="clear", font=("Arial", 14), command=self.clear)
        # add button to window
        self.clear_text_button.pack()



        # start warning method on app closing
        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)

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

    ## warning message popup window
    def on_closing(self):
        if messagebox.askyesno(title="WARNING", message="Do you really want to quit?"):
            self.root.destroy()

    # clear text method
    def clear(self):
        self.textbox.delete("1.0", tk.END)
win = MyGUI()