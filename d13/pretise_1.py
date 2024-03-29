import time
import tkinter
import tkinter.messagebox

def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('notice:', 'ok!')

def show_about():
    tkinter.messagebox.showinfo('about:', 'heh')

def main():
    top = tkinter.Tk()
    top.title('one')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)
    
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='download', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='about', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    
    tkinter.mainloop()


if __name__ == "__main__":
    main()
