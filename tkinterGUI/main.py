import tkinter as tk

root = tk.Tk()

# setup window size
root.geometry("800x500")
# add title
root.title("Tkinter practice")

# create content
label = tk.Label(root, text="Content", font=("Arial",18))
# add content to window
label.pack()

root.mainloop()