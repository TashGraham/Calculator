import tkinter as tk

# calculation string 
calculation = ""

def addToCalc(symb):
    global calculation
    calculation += str(symb) #adding symbol to the calculation string
    resultText.delete(1.0, "end")
    resultText.insert(1.0, calculation)

def evalCalc():
    global calculation
    try:
        calculation = str(eval(calculation))
        resultText.delete(1.0, "end")
        resultText.insert(1.0, calculation)
    except:
        # if calculation cannot be evaluated then there is an error with the calculation
        clearField()
        resultText.insert(1.0, "Error")

def clearField():
    global calculation
    calculation = ""
    resultText.delete(1.0, "end")

def dltLast():
    global calculation
    calculation = calculation[:-1]
    resultText.delete(1.0, "end")
    resultText.insert(1.0, calculation)


# making gui calc
root = tk.Tk()
root.geometry("325x275")

resultText = tk.Text(root, height=2, width=16, font=("Arial", 24))
resultText.grid(columnspan=6)

# creating buttons
btn_1 = tk.Button(root, text="1", command=lambda: addToCalc(1), width=5, font=("Arial", 14), bg="darkgray")
btn_1.grid(row=5, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: addToCalc(2), width=5, font=("Arial", 14), bg="darkgray")
btn_2.grid(row=5, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: addToCalc(3), width=5, font=("Arial", 14), bg="darkgray")
btn_3.grid(row=5, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: addToCalc(4), width=5, font=("Arial", 14), bg="darkgray")
btn_4.grid(row=4, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: addToCalc(5), width=5, font=("Arial", 14), bg="darkgray")
btn_5.grid(row=4, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: addToCalc(6), width=5, font=("Arial", 14), bg="darkgray")
btn_6.grid(row=4, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: addToCalc(7), width=5, font=("Arial", 14), bg="darkgray")
btn_7.grid(row=3, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: addToCalc(8), width=5, font=("Arial", 14), bg="darkgray")
btn_8.grid(row=3, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: addToCalc(9), width=5, font=("Arial", 14), bg="darkgray")
btn_9.grid(row=3, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: addToCalc(0), width=10, font=("Arial", 14), bg="darkgray")
btn_0.grid(row=6, column=1, columnspan=2, sticky = tk.W+tk.E)


btn_plus = tk.Button(root, text="+", command=lambda: addToCalc("+"), width=5, font=("Arial", 14), bg="orange")
btn_plus.grid(row=3, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: addToCalc("-"), width=5, font=("Arial", 14), bg="orange")
btn_minus.grid(row=3, column=5)
btn_mul = tk.Button(root, text="*", command=lambda: addToCalc("*"), width=5, font=("Arial", 14), bg="orange")
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: addToCalc("/"), width=5, font=("Arial", 14), bg="orange")
btn_div.grid(row=4, column=5)
btn_dot = tk.Button(root, text=".", command=lambda: addToCalc("."), width=5, font=("Arial", 14), bg="darkgray")
btn_dot.grid(row=6, column=3)
btn_open = tk.Button(root, text="(", command=lambda: addToCalc("("), width=5, font=("Arial", 14))
btn_open.grid(row=2, column=1)
btn_close = tk.Button(root, text=")", command=lambda: addToCalc(")"), width=5, font=("Arial", 14))
btn_close.grid(row=2, column=2)

btn_clr = tk.Button(root, text="CLR", command=clearField, width=10, font=("Arial", 14))
btn_clr.grid(row=2, column=4, columnspan=2, sticky = tk.W+tk.E)
btn_dlt = tk.Button(root, text="DLT", command=dltLast, width=5, font=("Arial", 14))
btn_dlt.grid(row=2, column=3)
btn_equ = tk.Button(root, text="=", command=evalCalc, width=5, height=3, font=("Arial", 14), bg="orange")
btn_equ.grid(row=5, column=4, rowspan=2)

root.mainloop()