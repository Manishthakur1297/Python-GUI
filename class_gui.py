from tkinter import *

class MyFrame(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self['width'] = 400
        self['height'] = 300
        self['bg'] = '#ffff00'
        
        def click():
            conn = mysql.connect('localhost','root','pass@123','aa')
            cur = conn.cursor()
            cur.execute('show tables')
            x = curr.fetchall()
            print(x)
        
        b=Button(self,text='Click Button',command=click)
        b.place(x=80,y=50)
#        self.pack()
        
            
        self.pack()

if __name__ == '__main__':
    root = Tk()
    root['bg'] = 'red'
    MyFrame(root)
    
    root.mainloop()