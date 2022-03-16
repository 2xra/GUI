import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create three int variables to use with the checkbuttons

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Option 1", variable=self.cb_var1
        )

        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Option 2", variable=self.cb_var2
        )
        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Option 3", variable=self.cb_var3
        )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.mybutton = tkinter.Button(
            self.main_window, text="okay", command=self.do_something
        )
        self.quitbutton = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )
        self.quitbutton.pack(side="right")
        self.mybutton.pack(side="left")

        self.bottom_frame.pack(side="bottom")
        self.top_frame.pack(side="top")

        tkinter.mainloop()

    def do_something(self):
        self.message = "you have selected:\n"

        if self.cb_var1.get() == 1:
            self.message += "1\n"
        if self.cb_var2.get() == 1:
            self.message += "2\n"
        if self.cb_var3.get() == 1:
            self.message += "3\n"
        tkinter.messagebox.showinfo("response", self.message)


yourmother = MyGUI()
