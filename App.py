import tkinter as tk


window = tk.Tk()
window.geometry("800x640")

title = tk.Label(master=window, text="Heart Calculator", width=100, height=5)
title.place(x=0,y=0)
title.pack()

label = tk.Label(master=window, text="Please fill in the entries below", width=100, height=5)
label.place(x=100,y=100)
label.pack()


button = tk.Button(text="Calculate", width=10, height=10)
AgeEntry = tk.Entry(bg='yellow', width=50)
button.pack()
AgeEntry.pack()
AgeEntry.insert(0,"Cool")

def calculate():
    age = AgeEntry.get()
    print(age)

window.mainloop()
