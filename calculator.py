import tkinter as tk
from turtle import *
from unittest import result

input_text=""


def add_to_field(test):
    global input_text
    input_text=input_text+str(test)
    field.delete("1.0","end")
    field.insert("1.0",input_text)

def calculate():
    global input_text
    result=str(eval(input_text))
    field.delete("1.0","end")
    field.insert("1.0",result)

def clear():
    global input_text
    input_text=""
    field.delete("1.0","end")
   

window=tk.Tk()
window.title('Calculator')
window.iconbitmap("callogo.ico")
window.geometry("300x250")
field=tk.Text(window,height=2,width=21,font=("Times new Roman",20))
field.grid(row=0,column=1,columnspan=4)

########################### 1 row

btn_rbrac=tk.Button(window,text="(",command=lambda: add_to_field("("),width=5,font=("Times new Roman",12))
btn_rbrac.grid(row=1,column=1)

btn_lbrac=tk.Button(window,text=")",command=lambda: add_to_field(")"),width=5,font=("Times new Roman",12))
btn_lbrac.grid(row=1,column=2)

btn_clear=tk.Button(window,text="C",command=lambda: clear(),width=5,bg="red",font=("Times new Roman",12))
btn_clear.grid(row=1,column=3)

btn_div=tk.Button(window,text="/",command=lambda: add_to_field("/"),width=5,font=("Times new Roman",12))
btn_div.grid(row=1,column=4)

########################### 2 row
btn_7=tk.Button(window,text="7",command=lambda: add_to_field(7),width=5,font=("Times new Roman",12))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(window,text="8",command=lambda: add_to_field(8),width=5,font=("Times new Roman",12))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(window,text="9",command=lambda: add_to_field(9),width=5,font=("Times new Roman",12))
btn_9.grid(row=2,column=3)

btn_multi=tk.Button(window,text="*",command=lambda: add_to_field("*"),width=5,font=("Times new Roman",12))
btn_multi.grid(row=2,column=4)

##########################  3 row

btn_4=tk.Button(window,text="4",command=lambda: add_to_field(4),width=5,font=("Times new Roman",12))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(window,text="5",command=lambda: add_to_field(5),width=5,font=("Times new Roman",12))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(window,text="6",command=lambda: add_to_field(6),width=5,font=("Times new Roman",12))
btn_6.grid(row=3,column=3)

btn_sub=tk.Button(window,text="-",command=lambda: add_to_field("-"),width=5,font=("Times new Roman",12))
btn_sub.grid(row=3,column=4)


##########################  4 row
btn_1=tk.Button(window,text="1",command=lambda: add_to_field(1),width=5,font=("Times new Roman",12))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(window,text="2",command=lambda: add_to_field(2),width=5,font=("Times new Roman",12))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(window,text="3",command=lambda: add_to_field(3),width=5,font=("Times new Roman",12))
btn_3.grid(row=4,column=3)

btn_add=tk.Button(window,text="+",command=lambda: add_to_field("+"),height=3,width=5,font=("Times new Roman",12))
btn_add.grid(row=4,column=4,rowspan=2)


##########################  5 row

btn_dec=tk.Button(window,text=".",command=lambda: add_to_field("."),width=5,bg="lightgreen",font=("Times new Roman",12))
btn_dec.grid(row=5,column=1)

btn_0=tk.Button(window,text="0",command=lambda: add_to_field(0),width=5,font=("Times new Roman",12))
btn_0.grid(row=5,column=2)

btn_equal=tk.Button(window,text="=",command=lambda: calculate(),width=5,bg="blue",font=("Times new Roman",12))
btn_equal.grid(row=5,column=3)


window.mainloop()