import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as tkFont
from pytube import YouTube
import os

def descargar():
    url = entry_url.get()
    yt = YouTube(url)
    out_path = filedialog.askdirectory(title='Seleccione la carpeta de descarga')

    if formato.get() == 1:
        video = yt.streams.get_audio_only()
        out_file = video.download(output_path=out_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)
    elif formato.get() == 2:
        video = yt.streams.get_audio_only()
        out_file = video.download(output_path=out_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    else:
        messagebox.showerror("Error", "Seleccione un formato de descarga.")
        return

    messagebox.showinfo("Descarga completa", yt.title + " ha sido descargado satisfactoriamente.")

root = tk.Tk()
root.resizable(False, False)
root.title("Youtube Sample Downloader - Test Unit")
font = tkFont.Font(family="Roboto", size=11)
root.option_add("*Font", font)
root.config(bg="#636363")
root.geometry("600x300")

label_url = tk.Label(root, text="\nINTRODUCE LA URL DEL VIDEO DE YOUTUBE: ", fg="white", bg="#636363")
label_url.grid(row=0, column=0, columnspan=2, pady=10, padx=140,sticky="NSEW")

entry_url = tk.Entry(root)
entry_url.grid(row=1, column=0, columnspan=2, pady=10, padx=140,sticky="NSEW")

formato = tk.IntVar()
formato.set(0)

rb_wav = tk.Radiobutton(root, text=".WAV", variable=formato, value=1)
rb_wav.grid(row=2, column=0, pady=20, padx=10,sticky="NSEW")

rb_mp3 = tk.Radiobutton(root, text=".MP3", variable=formato, value=2)
rb_mp3.grid(row=2, column=1, pady=20, padx=10,sticky="NSEW")

button_descargar = tk.Button(root, text="DESCARGAR", command=descargar)
button_descargar.grid(row=3, column=0, columnspan=2, pady=10, padx=10,sticky="NSEW")


root.mainloop()