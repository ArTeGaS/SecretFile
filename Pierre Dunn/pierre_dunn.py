from tkinter import *
import sys


def launcher():
    def clicked_yes():
        lbl.configure(text="Я знал)))")
        window.geometry('280x65')
        window.overrideredirect(False)

    def clicked_no():
        lbl.configure(text="Не пизди)))")
        window.geometry('210x39')
        window.overrideredirect(True)

    def clicked_exit():
        sys.exit()

    window = Tk()
    window.title("Хуй, кек - чебурек!")
    window.attributes("-topmost", True)
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - 50
    h = h - 50
    window.geometry(f'210x39+{w}+{h}')
    window.resizable(False, False)
    window.overrideredirect(True)
    lbl = Label(window, text="Ты даун?", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)
    btn = Button(window, text="Да", command=clicked_yes)
    btn1 = Button(window, text="Нет", command=clicked_no)
    btn2 = Button(window, text="---ВЫХОД---", command=clicked_exit)
    btn.grid(column=1, row=0)
    btn1.grid(column=2, row=0)
    btn2.grid(column=0, row=1)
    window.mainloop()


launcher()
