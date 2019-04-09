from tkinter import *
root = Tk()

root.minsize(width=400,height=300)
root.title('Calcii GUI App')

var_first = IntVar()
var_second = IntVar()
var_result = StringVar()

def Add():
#    x = int(first.get())
#    y = int(second.get())
#    res = x+y
#    
    a = var_first.get()
    b = var_second.get()
    var_result.set(a+b)
    
    #label_result.config(text=res)

first = Entry(root,width = 15,textvariable=var_first)
second = Entry(root,width = 15,textvariable=var_second)
btn_result = Button(root,text='Add',command=Add)
label_result = Label(root,textvariable=var_result)

first.pack()
second.pack()
btn_result.pack()
label_result.pack()

root.mainloop()
