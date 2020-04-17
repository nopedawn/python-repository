# Import tkinter & webbrowser
from tkinter import *
import webbrowser

# layarScreen Utama
layarScreen = Tk()
# Judul / Title
layarScreen.title("Search Bar")

# Function
def search():
    url = entry.get()
    webbrowser.open(url)

# Label
label1 = Label(layarScreen, text='Enter URL: ', font=('calibri', 10, 'italic', 'bold'))
label1.grid(row=0, column=0)

# Entry Bar
entry = Entry(layarScreen, width=30)
entry.grid(row=0, column=1)

# Tombol / Button
button = Button(layarScreen, text='Search', command=search)
button.grid(row=1, column=0, columnspan=2, pady=10)

# mainloop
layarScreen.mainloop()
