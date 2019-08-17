import recog
import time
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
w = tk.Frame(root,height="400", width="900", bg="red")
w.pack()
w.pack_propagate(0) 
lmain = tk.Label(w)
lmain.pack()
cap = cv2.VideoCapture(0)

def prin():
    cap = recog.ligar_camera()
    cont = 0
    lista = recog.guardar_participantes('okita.jpg', 'caio.jpg')

    while True: 
        rgb = recog.capturar_frame(cap)
        coord = recog.reconhecer_rosto(lista, rgb[0])
        frame = recog.desenhar(coord[0], coord[1], rgb[1])
        print('teste')
        recog.display(frame)
        
def popup():
    toplevel = Toplevel()
    label1 = Label(toplevel, height=0, width=100)
    label1.pack()
    label2 = Label(toplevel, height=0, width=100)
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
    f1 = tk.Frame(root, height="200",width="900", bg="white")
    f1.pack(side="left")
    f1.pack_propagate(0)
    button = tk.Button(w, text="oi", command= lambda: show_frame())
    button.pack()

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
root.geometry("1280x720")
main(root)
root.mainloop()

#python3 ex1.py
