import tkinter


window = tkinter.Tk()
window.title("Boy Kilo İndeksi")
window.config(bg="black")
window.minsize(500, 500)
font = ('Arial', 10, "normal")

label = tkinter.Label(text="Boy-Kilo İndeksi", fg="white", bg="black", padx=10, pady=10)
label.pack()

label1 = tkinter.Label(text="Boyunuzu Girin: ", fg="white", bg="black", padx=10, pady=10, font=(font))
label1.pack()




def boy_def():
    kilo = entry2.get()
    boy_print = entry1.get()
    print(boy_print)
    print(kilo)


entry1 = tkinter.Entry(width=15, bg="white", fg="black")
entry1.pack()


def button_def():
    boy_print = float(entry1.get())
    kilo = float(entry2.get())

    indeks = kilo / (boy_print ** 2)

    label4.config(text="İndeks: {:.2f}".format(indeks),padx=10,pady=10,bg="black",fg="white")

    if indeks < 18.5:
        label5 = tkinter.Label(text="ZAYIF :( \n Lütfen beslenmene dikkat et! :)")
        label5.pack()
    elif 18.5< indeks <24.9:
        label6 = tkinter.Label(text="NORMAL :) \n Sağlıklı günler! :)")
        label6.pack()
    elif 25< indeks <29.9:
        label7 = tkinter.Label(text="KİLOLU! \n Lütfen beslenmene dikkat et! :)")
        label7.pack()
    elif indeks > 30:
        label8 = tkinter.Label(text="OBEZ! \n Lütfen beslenmene dikkat et! :)")
        label8.pack()










label2 = tkinter.Label(text="Kilonuzu Girin:", bg="black", fg="white", font=(font), padx=10, pady=10)
label2.pack()

entry2 = tkinter.Entry(width=15)
entry2.pack()

button = tkinter.Button(text="OK", width=5, height=0, command=button_def,pady=5)
button.pack()

label3 = tkinter.Label(text="", bg="black", fg="white", font=(font))
label3.pack()

label4 = tkinter.Label(text="Lütfen boyunuzu nokta kullanarak yazınız\n Örnek(1.90-1.85-2.00 vs.)",font=(font))
label4.pack()


tkinter.mainloop()
