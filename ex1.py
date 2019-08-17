from tkinter import *
import recog
import time

root = Tk()

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

def main():
    w = Frame(root,height="300", width="300", bg="red")
    w.pack(padx="300")
    button = Button(w, text="oi", command= lambda: prin())
    button.pack(padx="50", pady="50")


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
main()
mainloop()

#python3 ex1.py
