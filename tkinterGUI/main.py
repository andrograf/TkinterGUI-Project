import tkinter as tk

root = tk.Tk()

# setup window size
root.geometry("800x500")
# add title
root.title("Tkinter practice")

# create content
label = tk.Label(root, text="Content", font=("Arial",18))
# add content to window
label.pack(padx=20, pady=20)
# create a textbox 
textbox = tk.Text(root, height=3, font=("Arial", 14) )
# add textbox to window
textbox.pack(padx=30)

root.mainloop()