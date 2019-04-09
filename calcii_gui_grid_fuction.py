from tkinter import *
#root = Tk()

root_win = Tk()
root_win['bg'] = 'yellow'

root = Frame(root_win,bg='blue',padx=25,pady=25)
root.pack()


#root.minsize(width=600,height=400)
#root.title('Calcii GUI App')

var_first = IntVar()
var_second = IntVar()
var_result = StringVar()

def Add():
    a = var_first.get()
    b = var_second.get()
    var_result.set('Sum  = '+str(a+b))
    
label_first = Label(root,text = 'First Num : ',font=('arial',16,'bold'),padx=6,pady=6,bg='blue',fg='white')
label_second = Label(root,text = 'Second Num : ',font=('arial',16,'bold'),padx=6,pady=6,bg='blue',fg='white')

first = Entry(root,width=20,font=('arial',16,'bold'),textvariable=var_first,borderwidth=4)
second = Entry(root,width=20,font=('arial',16,'bold'),textvariable=var_second,borderwidth=4)
btn_result = Button(root,font=('arial',16,'bold'),text='Add',bg='green',fg='white',command=Add,borderwidth=10)
label_result = Label(root,font=('arial',18,'bold'),textvariable=var_result,fg='white',padx=6,pady=6,bg='blue')

label_first.grid(row=0,column=0,pady=10)
first.grid(row=0,column=1,pady=10)

label_second.grid(row=1,column=0,pady=10)
second.grid(row=1,column=1,pady=10)

btn_result.grid(row=2,columnspan=2)    # Sticky ---- East,WEST,NORTH,SOUTH
label_result.grid(row=4,columnspan=2)

root.mainloop()
