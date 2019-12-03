import tkinter
import tkinter.messagebox

def main():
    flag = True
    
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('green', 'i am heh.') if flag else ('black', 'i am allen')
        label.config(text=msg, fg=color)
        
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('please:', 'exit?'):
            top.quit()
    
    top = tkinter.Tk()
    top.geometry('300x300')
    top.title('Game yss')
    label = tkinter.Label(top, text='i am hey.', font='Arial -32', fg='yellow')
    label.pack(expand=10)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='next', command=change_label_text)
    button1.pack(side='top')
    button2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()
