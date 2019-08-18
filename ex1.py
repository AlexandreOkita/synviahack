import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage


root = tk.Tk()
w = tk.Frame(root,height="400", width="1893", bg="red")
w.pack()
w.pack_propagate(0) 
foto = ImageTk.PhotoImage(Image.open("dados.jpg"))
lmain = tk.Label(w)
lmain.pack()
cap = cv2.VideoCapture(0)


def popup():
    toplevel = tk.Toplevel()
    label1 = tk.Label(toplevel, height=0, width=100)
    label1.pack()
    label2 = tk.Label(toplevel, height=0, width=100)
    label2.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 

def main(root):
    f1 = tk.Frame(root, height="343",width="1893", bg="white")
    f1.pack(side="left")
    f1.pack_propagate(0)
    button = tk.Button(w, text="oi", command= lambda: show_frame())
    button.pack()
    dados = tk.Button(f1, image=foto, bg="#ddd9ce", tearoff="0", border="0")
    dados.pack(fill=tk.BOTH)
    dados.pack_propagate(1)

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
root.geometry("1893x743")
main(root)
root.mainloop()

#python3 ex1.py;.