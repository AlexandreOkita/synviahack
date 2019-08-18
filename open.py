import os
import tkinter as st
from PIL import ImageTk, Image
from tkinter import PhotoImage
from subprocess import call

root = st.Tk()
foto = ImageTk.PhotoImage(Image.open("fundo.jpeg"))


def chamada():
    root.after(200,root.destroy())
    call(["python3", "teste.py"])
  
root.geometry("1300x769")
fr = st.Label(root,width="1300", height="769", image=foto)
fr.pack()
fr.pack_propagate(0)
bt = st.Button(fr, height="5", bg="#9F5F9F", fg="white", width="20", text="Iniciar", command = lambda: chamada())
bt.pack(padx=551, side=st.BOTTOM)
root.geometry("1300x769")
root.mainloop()