import numpy as np
import cv2
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage
import recog
import ObjectDetector

process_frame = 0
cont = 0
root = tk.Tk()
w = tk.Frame(root,height="400", width="1280", bg="black")
w.pack()
w.pack_propagate(0) 
foto = ImageTk.PhotoImage(Image.open("dados.jpg"))
pop = ImageTk.PhotoImage(Image.open("popup.jpg"))
lmain = tk.Label(w)
lmain.pack()
cap = recog.ligar_camera()
lista = recog.guardar_participantes('okita.jpg', 'caio.jpg')
od = ObjectDetector.Object_Detector()

def popup():
    toplevel = tk.Toplevel()
    label1 = tk.Label(toplevel, height=0, bg="white", width=100)
    label1.pack()
    label2 = tk.Label(toplevel, height=0, bg="white", width=100)
    label2.pack()
    label3 = tk.Label(toplevel, image=pop, bg="white", height="130px")
    label3.pack(side=tk.TOP)
def show_frame(frame):
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        root.update()

def prin():
        global process_frame
        global cont
        ret, frame = recog.capturar_frame(cap)
        coord = recog.reconhecer_rosto(lista, ret)
        if process_frame%5 == 0:
            frame = od.process(frame)
            process_frame = 0
        else:
            frame = recog.desenhar(coord[0], coord[1], frame)            
            
        process_frame += 1
        print('NAMES:',coord[1])
        print('CONT:',cont)
        for i in coord[1]:
                if i == "Unknown":
                        cont += 1
                        if (cont == 10):
                                popup()
                                cont = -1
                                
                elif cont != -1:
                        cont = 0
                
        show_frame(frame)

def main(root):
    dados = tk.Label(root, image=foto, bg="#E6E8FA", height="233", width="1280")
    dados.pack(fill=tk.Y)
    dados.pack_propagate(0)
    while 1:
        prin()

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
root.geometry("1280x633")
main(root)
root.mainloop()

#python3 ex1.py;.
