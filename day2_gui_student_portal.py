from tkinter import *
import tkinter.messagebox as tm

root = Tk()
root.state('zoomed')
root['bg'] = '#fff0f0'

root_frame = Frame(root,width=600,height=400,bg='#47CD37',padx=25,pady=25)
root_frame.place(x=450,y=250)

var_user = StringVar()
var_pass = StringVar()

def cmd_user_login():
    login_user = var_user.get()
    login_pass= var_pass.get()
    var_user.set('')
    var_pass.set('')
    if not (login_user!='' and login_pass=='12345'):
        tm.showerror('Failed!!!','User Id or Password is Wrong\n Please try later!')
        return
    tm.showinfo('Success','Welcome {} \n You have successfully logged in'.format(login_user))
    return



def cmd_new_user():
    new_user_win = Toplevel()
    new_user_win['bg'] = 'gray'
    
    frame_new_user = Frame(new_user_win,width=450,height=350)
    frame_new_user.pack()
    
    img = PhotoImage(file=r"C:\Users\acer\Pictures\techyshed.png")
    
    new_label = Label(new_user_win)
    new_label.pack()
    
    def left_click(a):
        #tm.showinfo('Mouse Click!','Left Click')
        new_label.config(image=img)
        new_label.image = img
    
    def middle_click(a):
        tm.showinfo('Mouse Click!','Middle Click')
        
    def right_click(a):
        tm.showinfo('Mouse Click!','Right Click')
        
    frame_new_user.bind('<Button-1>',func=left_click)
    frame_new_user.bind('<Button-2>',func=middle_click)
    frame_new_user.bind('<Button-3>',func=right_click)
    
    btn = Button(new_user_win,text='Exit',command=new_user_win.destroy,bg='red',fg='white')
    btn.pack()
    
    new_user_win.mainloop()
    
    
def about_us():
    tm.showinfo('About Us ! ','We are Legion')


label = Label(root_frame,text='Student Login portal',font=('arial,18,bold'),bg='#47CD37',fg='white',padx=14,pady=14) #.place(x=50,y=20)

label_user = Label(root_frame,text='User Id : ',font=('arial,18,bold'),bg='#47CD37',fg='white',padx=14,pady=14)
label_password = Label(root_frame,text='Password : ',font=('arial,18,bold'),bg='#47CD37',fg='white',padx=14,pady=14)

entry_user = Entry(root_frame,textvariable=var_user)
entry_password = Entry(root_frame,show='*',textvariable=var_pass)

btn_login = Button(root_frame,text='Login',font=('arial,18,bold'),bg='#47CD37',fg='white',padx=12,pady=8,command = cmd_user_login)
btn_new_user = Button(root_frame,text='New User ? ',font=('arial,18,bold'),bg='#47CD37',fg='white',padx=12,pady=8,command = cmd_new_user)

label.grid(row=0,columnspan=2)
label_user.grid(row=1,column=0)
label_password.grid(row=2,column=0)

entry_user.grid(row=1,column=1)
entry_password.grid(row=2,column=1)

btn_login.grid(row=3,columnspan=2,sticky=NSEW)
btn_new_user.grid(row=4,columnspan=2,sticky=NSEW)


menuBar = Menu(root)
file_menu = Menu(menuBar,tearoff=False)

menuBar.add_cascade(menu=file_menu,label='File')
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Exit',command=quit)

help_menu = Menu(menuBar,tearoff=False)
menuBar.add_cascade(menu=help_menu,label='Help')
help_menu.add_command(label='About',command=about_us)
help_menu.add_command(label='Contact')
help_menu.add_command(label='Update')

root.config(menu=menuBar)


root.mainloop()