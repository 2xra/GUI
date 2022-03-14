import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text="John")

        self.label2 = tkinter.Label(self.top_frame, text="Jill")
        self.label3 = tkinter.Label(self.top_frame, text="James")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4 = tkinter.Label(self.bottom_frame, text="Jack")
        self.label5 = tkinter.Label(self.bottom_frame, text="Jim")
        self.label6 = tkinter.Label(self.bottom_frame, text="Jerry")
        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.mybutton = tkinter.Button(
            self.main_window, text="click me!", command=self.do_something
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
        tkinter.messagebox.showinfo("response", "thanks for hitting that")


yourmother = MyGUI()
