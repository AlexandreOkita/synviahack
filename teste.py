import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage

root = tk.Tk()
w = tk.Frame(root,height="400", width="900", bg="black")
w.pack()
w.pack_propagate(0) 
foto = ImageTk.PhotoImage(Image.open("dados.jpg"))
lmain = tk.Label(w)
lmain.pack()


def popup():
    toplevel = tk.Toplevel()
    label1 = tk.Label(toplevel, height=0, width=100)
    label1.pack()
    label2 = tk.Label(toplevel, height=0, width=100)
    label2.pack()

def show_frame(frame):
        print('teste')
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        root.update()

def prin():
        cont = 0
        rgb = recog.capturar_frame(cap)
        coord = recog.reconhecer_rosto(lista, rgb[0])
        frame = recog.desenhar(coord[0], coord[1], rgb[1])
        show_frame(frame)

def main(root):
    dados = tk.Label(root, image=foto, bg="#E6E8FA", height="343")
    dados.pack(fil=tk.Y)
    dados.pack_propagate(0)

#class Example(tk.Frame):
    #def __init__(self, parent):
     #   tk.Frame.__init__(self, parent)
      #  new_win_button = tk.Button(self, text="Create new window", command=self.new_window)
       # new_win_button.pack()

   # def new_window(self):
    #    top = tk.Toplevel(self)
     #   label = tk.Label(top, text="Hello, world")
      #  b = tk.Button(top, text="Destroy me", 
       #               command=lambda win=top: win.destroy())
        #label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        #b.pack(side="bottom")

#if __name__ == "__main__":
 #   root = tk.Tk()
  #  Example(root).pack(fill="both", expand=True)
   # root.mainloop()
root.geometry("900x638")
main(root)
root.mainloop()

#python3 ex1.py;.