from tkinter import *
import tkinter.messagebox as tm

root = Tk()
#root.state('zoomed')
root['bg'] = 'blue'
root.geometry('600x400+300+200') #widthxheight+x+y
#root.maxsize(width=600,height=400)
root.minsize(width=400,height=300)
root.title('First GUI App')

def hello():
#    x=tm.askyesnocancel('Alert','Do you want to execute ? ')
#    if not x:
#        return
    #global x
    #x+=1
    x=entry.get()
    label.config(text = x)
#    label.config(text = 'Hello World ' + str(x))
    print('Hello Button')
    
entry = Entry(root,width=50,font=('arial'))
entry.pack()


btn = Button(root,text='Click Me',font=('arial',20,'bold'),bg='green',
             fg='white',command = hello)  # ,command=quit())
#btn.pack(side=BOTTOM)
btn.pack(pady=50,fill=X)
#text
#x=0
label = Label(root,text='Write in Text Box First !',bg='blue',fg='white')
label.pack()



root.mainloop()