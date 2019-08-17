from tkinter import *

root = Tk()

def prin():
    print("OI")
def main():
    w = Frame(root, height="768", width="1367", bg="red")
    w.pack()
    w.pack_propagate(0)
    g = Frame(w,  height="768", width="1367", bg="blue")
    g.pack()
    g.pack_propagate(1)
    button = Button(g, text="oi", command= prin())
    button.pack(padx="250", pady="350")


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
main()
mainloop()

#python3 ex1.py