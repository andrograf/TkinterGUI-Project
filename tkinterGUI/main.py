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

# create a frame(grid) for buttons
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

# create buttons
button = tk.Button(buttonFrame, text="Increase", font=("Arial", 14))
button2 = tk.Button(buttonFrame, text="Decrease", font=("Arial", 14))
button3 = tk.Button(buttonFrame, text="Reset", font=("Arial", 14))

# add button to frame
button.grid(row=0, column=0, sticky=tk.W+tk.E)
button2.grid(row=0, column=1, sticky=tk.W+tk.E)
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

# add frame to window
buttonFrame.pack(padx=30, pady=20, fill="x")

root.mainloop()