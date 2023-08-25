from tkinter import *


def button_click(number):

    global equation_text
    equation_text = equation_text + str(number)
    equation_label.set(equation_text)

def equals():

    global equation_text
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text = total

def clear():

    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x650")
window.config(background="black")

equation_text = ""

equation_label = StringVar()

label = Label(window,
              textvariable=equation_label,
              font=("roboto", 40, "bold"),
              fg="white",
              bg="black",
              relief=RAISED,
              bd=10,
              width=13,
              height=2)
label.pack()

frame = Frame(window)
frame.pack()

button_1 = Button(frame, text=1, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(1))
button_1.grid(row=0, column=0)
button_2 = Button(frame, text=2, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(2))
button_2.grid(row=0, column=1)
button_3 = Button(frame, text=3, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(3))
button_3.grid(row=0, column=2)
button_4 = Button(frame, text=4, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(4))
button_4.grid(row=1, column=0)
button_5 = Button(frame, text=5, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(5))
button_5.grid(row=1, column=1)
button_6 = Button(frame, text=6, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(6))
button_6.grid(row=1, column=2)
button_7 = Button(frame, text=7, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(7))
button_7.grid(row=2, column=0)
button_8 = Button(frame, text=8, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(8))
button_8.grid(row=2, column=1)
button_9 = Button(frame, text=9, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(9))
button_9.grid(row=2, column=2)
button_0 = Button(frame, text=0, height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=lambda: button_click(0))
button_0.grid(row=3, column=0)


addition_button = Button(frame, text="+", height=2, width=4, font=("roboto", 30),
                  fg="white", bg="#b85e11", command=lambda: button_click("+"))
addition_button.grid(row=0, column=3)

subtraction_button = Button(frame, text="-", height=2, width=4, font=("roboto", 30),
                  fg="white", bg="#b85e11", command=lambda: button_click("-"))
subtraction_button.grid(row=1, column=3)

multiplication_button = Button(frame, text="*", height=2, width=4, font=("roboto", 30),
                  fg="white", bg="#b85e11", command=lambda: button_click("*"))
multiplication_button.grid(row=2, column=3)

division_button = Button(frame, text="/", height=2, width=4, font=("roboto", 30),
                  fg="white", bg="#b85e11", command=lambda: button_click("/"))
division_button.grid(row=3, column=3)


equals_button = Button(frame, text="=", height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=equals)
equals_button.grid(row=3, column=2)
clear_button = Button(frame, text="AC", height=2, width=4, font=("roboto", 30),
                  fg="gray", bg="#1c1c1c", command=clear)
clear_button.grid(row=3, column=1)


window.mainloop()
