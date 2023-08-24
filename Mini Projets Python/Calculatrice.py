from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):
    current =result_lbl["text"]
    new=current+str(digit)
    result_lbl.config(text=new)
def clear():
    result_lbl.config(text="")

def get_operator(op):
    global  first_number,operator
    first_number = int(result_lbl["text"])
    operator=op
    result_lbl.config(text="")
def get_result():
    global  first_number,second_number,operator

    second_number=int (result_lbl["text"])
    if operator=="+":
        result_lbl.config(text=str(first_number+second_number))
    elif operator=="-":
        result_lbl.config(text=str(first_number-second_number))
    elif operator=="*":
        result_lbl.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            result_lbl.config(text="Error")
        else:
            result_lbl.config(text=str(round(first_number/second_number,2)))




root=Tk()
root.title("calculator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")

result_lbl=Label(root,text="",bg="black",fg="white")
result_lbl.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky="w")
result_lbl.config(font=("verdana",30,"bold"))

btn7 = Button(root,text="7",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=("verdana",14))

btn8 = Button(root,text="8",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=("verdana",14))

btn9 = Button(root,text="9",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=("verdana",14))

btn_add = Button(root,text="+",bg="#ebde33",fg="black",width=5,height=2,command=lambda :get_operator("+"))
btn_add.grid(row=1,column=3)
btn_add.config(font=("verdana",14))

btn4 = Button(root,text="4",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=("verdana",14))

btn5 = Button(root,text="5",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=("verdana",14))

btn6 = Button(root,text="6",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=("verdana",14))

btn_subb = Button(root,text="-",bg="#ebde33",fg="black",width=5,height=2,command=lambda :get_operator("-"))
btn_subb .grid(row=2,column=3)
btn_subb .config(font=("verdana",14))

btn1 = Button(root,text="1",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=("verdana",14))

btn2 = Button(root,text="2",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=("verdana",14))

btn3 = Button(root,text="3",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=("verdana",14))

btn_mult = Button(root,text="x",bg="#ebde33",fg="black",width=5,height=2,command=lambda :get_operator("*"))
btn_mult.grid(row=3,column=3)
btn_mult.config(font=("verdana",14))

btn_clr = Button(root,text="←",bg="#eb6733",fg="black",width=5,height=2,command=lambda: clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=("verdana",14))

btn0 = Button(root,text="0",bg="#ccc",fg="black",width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=("verdana",14))

btn_equals = Button(root,text="=",bg="#aae8f0",fg="black",width=5,height=2,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=("verdana",14))

btn_div = Button(root,text="/",bg="#ebde33",fg="black",width=5,height=2,command=lambda :get_operator("/"))
btn_div.grid(row=4,column=3)
btn_div.config(font=("verdana",14))


root.mainloop()