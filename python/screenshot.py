# Import tkinter dan pyautogui
import tkinter as tk
import pyautogui


# Pembuka tkinter
layarScreen = tk.Tk()

# Judul tkinter  
layarScreen.title("Tkinter ScreenCapture")
# Konfigurasi untuk tkinter
layarScreen.configure(background='blue')
# Ukuran layar tkinter
layarScreen.geometry('300x300')


# function
def takeScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    eventScreenshot()

def eventScreenshot():
    label1 = tk.Label(layarScreen, text='screenshot berhasil')
    label1.pack()

# Tombol untuk menjalankan function
tombol = tk.Button(layarScreen, text='Tekan untuk Screenshot', command=takeScreenshot)
tombol.pack()

# penutup tkinter menggunakan 'nama + .mainloop'
layarScreen.mainloop()
