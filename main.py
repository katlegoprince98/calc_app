from tkinter import *


def btnClick(numbers=None):
    global operator
    operator += str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_input.set("")


def btnEqual():
    global operator
    num = str(eval(operator))
    text_input.set(num)
    operator = ""


cal = Tk()
cal.title("DIPALO")
operator = ""
text_input = StringVar()

textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=2, insertwidth=4, bg='white',
                    fg='black',
                    justify='right')
textDisplay.grid(columnspan=4)

btn7 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="7", command=lambda: btnClick(7))
btn7.grid(row=1, column=0)

btn8 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda: btnClick(8))
btn8.grid(row=1, column=1)

btn9 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda: btnClick(9))
btn9.grid(row=1, column=2)

btnAdd = Button(cal, padx=16, fg="orange", bg='white', font=('arial', 20, 'bold'), text="+",
                command=lambda: btnClick("+"))
btnAdd.grid(row=1, column=3)

btn4 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="4", command=lambda: btnClick(4))
btn4.grid(row=2, column=0)

btn5 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="5", command=lambda: btnClick(5))
btn5.grid(row=2, column=1)

btn6 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="6", command=lambda: btnClick(6))
btn6.grid(row=2, column=2)

btnMul = Button(cal, padx=16, fg="orange", bg='white', font=('arial', 20, 'bold'), text="*",
                command=lambda: btnClick("*"))
btnMul.grid(row=2, column=3)

btn1 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="1", command=lambda: btnClick(1))
btn1.grid(row=3, column=0)

btn2 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="2", command=lambda: btnClick(2))
btn2.grid(row=3, column=1)

btn3 = Button(cal, padx=16, fg="black", font=('arial', 20, 'bold'), text="3", command=lambda: btnClick(3))
btn3.grid(row=3, column=2)

btnDev = Button(cal, padx=16, fg="orange", bg='white', font=('arial', 20, 'bold'), text="/",
                command=lambda: btnClick("/"))
btnDev.grid(row=3, column=3)

btnClr = Button(cal, padx=16, pady=16, fg="red", font=('arial', 18, 'bold'), text="AC", command=btnClear)
btnClr.grid(row=4, column=0)

btn0 = Button(cal, padx=16, pady=16, fg="black", font=('arial', 20, 'bold'), text="0", command=lambda: btnClick(0))
btn0.grid(row=4, column=1)

btnMin = Button(cal, padx=16, pady=16, fg="black", font=('arial', 20, 'bold'), text="-", command=lambda: btnClick("-"))
btnMin.grid(row=4, column=2)

btnEqu = Button(cal, padx=16, pady=16, fg="blue", bg='white', font=('arial', 20, 'bold'), text="=", command=btnEqual)
btnEqu.grid(row=4, column=3)

cal.mainloop()
