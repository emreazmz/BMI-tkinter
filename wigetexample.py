import tkinter
window = tkinter.Tk()
window.title("Python Tkinter")
window.config(bg="light pink")
window.minsize(600,600)
window.config(padx=10,pady=10)

label = tkinter.Label()
label.config(text="my label",fg="white",bg="light pink", font=('Ariel',10,"normal") ,pady=10,padx=10)

label.pack()

def button_click():
    print("button click")
    print(text.get("1.0",'end-1c'))

button = tkinter.Button(text=  "bas", width=10, height=1 ,command=button_click, bg="white",
fg="light pink",activebackground="light pink")
button.config(padx=10,pady=10)
button.pack()

entry = tkinter.Entry(width=20,bg="white")
#focus nereye focus atmak istersen
entry.focus()
entry.pack()

# text uzun yazılar için
text = tkinter.Text(width=50,height=10,padx=10,pady=10)
text.pack()

#scale
def scale_selected(value):
    print(value)
scale = tkinter.Scale(from_=0,to=50,command=scale_selected)
scale.pack()

#spinbox
def spinbox_selected():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0,to=50,command=spinbox_selected)
spinbox.pack()

#checkbutton
def my_checkbutton():
    print(check1.get())

check1 = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="check",command=my_checkbutton,padx=10,pady=10,variable=check1)
checkbutton.pack()

#radio button

def radio_but():
    print(r1.get())
r1 = tkinter.IntVar()
radiobutton = tkinter.Radiobutton(text="1. option",value=10,variable=r1,command=radio_but)
radiobutton2 = tkinter.Radiobutton(text="2. option",value=20,variable=r1,command=radio_but)
radiobutton.pack()
radiobutton2.pack()

#listbox

def listboxdef(event):
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox()
listbox.bind()
name_list = ["emre","yaşar","öykü","murat"]
for i in range(len(name_list)):
    listbox.insert(i,name_list[i])
    listbox.pack()


window.mainloop()