import tkinter
import tkinter.messagebox


class kiloconverter:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x600")
        self.main_window.title("Student Test Average")
        self.fontchoice = ("Comic Sans MS", 25)

        self.buttonbgcolor = "#154734"
        self.textcolor = "#FFB81C"
        self.main_window.configure(bg=self.buttonbgcolor)
        self.top_frame1 = tkinter.Frame(self.main_window)
        self.top_frame2 = tkinter.Frame(self.main_window)
        self.top_frame3 = tkinter.Frame(self.main_window)
        self.top_frame4 = tkinter.Frame(self.main_window)

        self.promptlabel1 = tkinter.Label(
            self.top_frame1,
            text="Enter the score for test 1:",
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.promptlabel2 = tkinter.Label(
            self.top_frame2,
            text="Enter the score for test 2:",
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.promptlabel3 = tkinter.Label(
            self.top_frame3,
            text="Enter the score for test 3:",
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.averagestrlabel = tkinter.Label(
            self.top_frame4,
            text="Average",
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.test_entry1 = tkinter.Entry(
            self.top_frame1,
            width=10,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.test_entry2 = tkinter.Entry(
            self.top_frame2,
            width=10,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.test_entry3 = tkinter.Entry(
            self.top_frame3,
            width=10,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.promptlabel1.pack(side="left")
        self.promptlabel2.pack(side="left")
        self.promptlabel3.pack(side="left")
        self.averagestrlabel.pack(side="left")
        self.average_var = tkinter.StringVar()

        self.test_entry1.pack(side="left")
        self.test_entry2.pack(side="left")
        self.test_entry3.pack(side="left")

        self.averagelabel = tkinter.Label(
            self.top_frame4,
            textvariable=self.average_var,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.averagelabel.pack(side="left")
        self.calcbutton = tkinter.Button(
            self.main_window,
            text="average",
            command=self.average,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.quitbutton = tkinter.Button(
            self.main_window,
            text="Quit",
            command=self.main_window.destroy,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.top_frame1.pack(side="top")
        self.top_frame2.pack(side="top")
        self.top_frame3.pack(side="top")
        self.top_frame4.pack(side="top")
        self.quitbutton.pack(side="right")
        self.calcbutton.pack(side="left")

        tkinter.mainloop()

    def average(self):
        averagecal = round(
            (
                float(self.test_entry3.get())
                + float(self.test_entry2.get())
                + float(self.test_entry1.get())
            )
            / 3,
            2,
        )

        self.average_var.set(averagecal)


yourmother = kiloconverter()
