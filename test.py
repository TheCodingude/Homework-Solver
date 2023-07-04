from tkinter import *
from tkinter.ttk import Notebook

window = Tk()
window.geometry("400x400")


note = Notebook(window)
note.pack(expand=True, fill="both")
note.add(Label(text=""), text="Essay Writer")
note.add(Label(text="hehehe"), text="Calculator")

note2 = Notebook()
note.add(note2, text="Chemistry")
note2.add(Label(text="LOLOLOLOL"), text="Stoichemtry")

note2.add(Label(text="HEHEHEH"), text="Equation Balancer")



window.mainloop()