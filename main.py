import math
import tkinter as tk
from tkinter import *

# PENCERE

window = tk.Tk()
window.geometry('300x400')
window.title("Hipotenus Bulma")
window.config(padx=40, pady=40)

def hipotenusBul():
    a = ilkinput.get()
    b = digerinput.get()


    if a == "" or b == "":
        sonuc_label.config(text ="Lütfen ikisi içinde değer giriniz.", font=("Bold", 10))
    else:
        try:
            c = math.sqrt(float(a)**2 + float(b)**2)
            sonuc_label.config(text=f"Hipotenüs: {round(c, 3)}", font=("Bold", 13))
        except:
            sonuc_label.config(text="Lütfen sayı giriniz", font=("Bold", 10))

# LABEL VE İNPUTLAR

ilkkenar = tk.Label(window, text="1.Kenarı Giriniz", font=("Bold", 15))
ilkkenar.pack()

ilkinput=tk.Entry(window, width=15)
ilkinput.pack()

digerkenar = tk.Label(window, text="2.Kenarı Giriniz", font=("Bold", 15))
digerkenar.pack()

digerinput=tk.Entry(window, width=15)
digerinput.pack()

# BUTON

button = tk.Button(window, text="Hesapla", font=("Verdana", 15), command=hipotenusBul)
button.pack(pady=10)

sonuc_label = tk.Label()
sonuc_label.pack()

# İKON

photo = PhotoImage(file="photoimage.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100,100, image=photo)
canvas.pack()

window.mainloop()









