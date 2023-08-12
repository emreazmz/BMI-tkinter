import tkinter

# Window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(500, 500)

def button_click():
    input_value = my_entry.get()
    print(input_value)

# Label
my_label = tkinter.Label(text="Ad Soyad: ")
my_label.config(fg="black", font=('Arial', 30, "bold"))
#my_label.pack(side="top")
#my_label.place(x=0,y=0)
my_label.grid(row=0,column=0)

# Button
my_button = tkinter.Button(text="Bas", fg="black", command=button_click, font=('Arial', 10, "italic"))
#my_button.pack(side="top")
#my_button.place(x=250-21,y=250-21)
#my_button.update()
#print(my_button.winfo_height())
my_button.grid(row=1, column=1)

# Entry
my_entry = tkinter.Entry()
#my_entry.pack(side="top")
#my_entry.place(x=150,y=150)
my_entry.grid(row=0,column=1)


window.mainloop()
