# library yang harus digunakan / library that you must use = tkinter, pypng, pyqrcode, pillow
import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk

# layarScreen tkinter = module
layarScreen = Tk()
layarScreen.title("QR Code Generator")
layarScreen.config(background='#b8285d')

# function
def generate():
    text = entry1.get()
    qr = pyqrcode.create(text)
    file_name = "my qrcode"
    save_path = r"C:\Users\Lenovo\Desktop\ "
    name = save_path + file_name + '.png'

    # pypng library = pip install pypng
    qr.png(name, scale=10)
    image = Image.open(name)
    image = image.resize((400,400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    layarScreen.imagelabel.config(image=image)
    layarScreen.imagelabel.photo = image

text = ttk.Label(layarScreen, text="Masukkan Text atau Link: ")
text.grid(row=0, column=0, padx=3, pady=3)

entry1 = ttk.Entry(layarScreen, width=40)
entry1.grid(row=0, column=1, padx=3, pady=3)

button = ttk.Button(layarScreen, text="Generate", command=generate)
button.grid(row=0, column=2, padx=3, pady=3)

show_qr = ttk.Label(layarScreen, text="QR Code: ")
show_qr.grid(row=1, column=0, padx=3, pady=3)

layarScreen.imagelabel = ttk.Label(layarScreen, background='#b8285d')
layarScreen.imagelabel.grid(row=2, column=0, padx=3, pady=3, columnspan=3)


# layarScreen mainloop = method
layarScreen.mainloop()
