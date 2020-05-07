# mengimport class tkinter
import tkinter


# awalan tkinter
layarUtama = tkinter.Tk()

# fungsi
def fungsiTekan():
	label2 = tkinter.Label(layarUtama, text="tombol telah ditekan")
	label2.pack()

# tombol
tombol = tkinter.Button(layarUtama, text="tekan tombol ini", command = fungsiTekan)
tombol.pack()

# teks halo dunia
label1 = tkinter.Label(layarUtama, text="halo dunia")
label1.pack()

# akhiran tkinter
layarUtama.mainloop()
