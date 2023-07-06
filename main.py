from tkinter import *
from tkinter.ttk import Notebook

from chatgpt import api_call
from calculator import parse_expr


def temp():
    
    thesis = thesis_input.get(1.0 , END)
    essay = api_call(thesis)
    essay_lbl.config(state="normal")
    essay_lbl.delete(1.0, END)
    essay_lbl.insert(END, essay)
    essay_lbl.config(state='disabled')

def calculate(symbol):
    global expr, expr_lbl
    if symbol == "SOLVE":
        result = parse_expr(expr)
        expr_lbl.config(text=result)
        expr = ""
        return
    symbol = str(symbol)
    expr+=symbol
    expr_lbl.config(text=expr)
    
def calc(key):
    # print(notebook.index(notebook.select()))
    if notebook.index(notebook.select()) != 1:
        return
    calculate(key.keysym)

expr = ""
window = Tk()
window.geometry("400x400")
window.title("Homework Do-er 9000")


notebook = Notebook(window)
notebook.pack(fill="both", expand=TRUE)


english_note = Notebook()


# Essay Writer
essay_frame = Frame()

thesis_input = Text(essay_frame, height=2, width=40)
thesis_input.pack()

submit_btn = Button(essay_frame, text="Write Essay", command=temp)
submit_btn.pack(pady=5)

Label(essay_frame, text="Final Essay: ").pack(pady=25)

essay_lbl = Text(essay_frame, bg="white", height=30, state="disabled")
essay_lbl.pack(fill="both", padx=5, pady=5)

english_note.add(essay_frame, text="Essay Writer")

notebook.add(english_note, text="English")
#Calculator 
#This is gonna be so fucking painful 

frame2 = Frame()
key_frame = Frame(frame2)

window.bind("<Key>", calc)

expr_lbl = Label(frame2, text="", width=20, bg="white")
expr_lbl.pack()

Button(key_frame, text="1", command=lambda: calculate(1)).grid(row=5, column=1)
Button(key_frame, text="2", command=lambda: calculate(2)).grid(row=5, column=2)
Button(key_frame, text="3", command=lambda: calculate(3)).grid(row=5, column=3)
Button(key_frame, text="4", command=lambda: calculate(4)).grid(row=5, column=4)
Button(key_frame, text="5", command=lambda: calculate(5)).grid(row=5, column=5)
Button(key_frame, text="6", command=lambda: calculate(6)).grid(row=5, column=6)
Button(key_frame, text="7", command=lambda: calculate(7)).grid(row=5, column=7)
Button(key_frame, text="8", command=lambda: calculate(8)).grid(row=5, column=8)
Button(key_frame, text="9", command=lambda: calculate(9)).grid(row=5, column=9)
Button(key_frame, text="0", command=lambda: calculate(0)).grid(row=5, column=10)

Button(key_frame, text="+", command=lambda: calculate("+")).grid(row=6, column=1)
Button(key_frame, text="-", command=lambda: calculate("-")).grid(row=6, column=2)
Button(key_frame, text="*", command=lambda: calculate("*")).grid(row=6, column=3)
Button(key_frame, text="/", command=lambda: calculate("/")).grid(row=6, column=4)
Button(key_frame, text="^", command=lambda: calculate("^")).grid(row=6, column=5)
Button(key_frame, text="(", command=lambda: calculate("(")).grid(row=6, column=6)
Button(key_frame, text=")", command=lambda: calculate(")")).grid(row=6, column=7)

Button(key_frame, text="SOLVE", command=lambda: calculate("SOLVE")).grid(row=6, column=8)

key_frame.pack()



notebook.add(frame2, text="Calculator")

window.mainloop()