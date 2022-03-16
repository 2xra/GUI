import tkinter
import tkinter.messagebox


class kiloconverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)

        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        # set the intvar  object to 1

        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Option1", variable=self.radio_var, value=10
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Option2", variable=self.radio_var, value=20
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="Option3", variable=self.radio_var, value=30
        )

        # sets default button
        self.rb3.select()

        self.okbutton = tkinter.Button(
            self.bottom_frame, text="OK", command=self.show_choice
        )

        self.resetbutton = tkinter.Button(
            self.bottom_frame, text="Reset", command=self.rb1.select
        )
        self.quitbutton = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.okbutton.pack()
        self.quitbutton.pack(side="bottom")
        self.resetbutton.pack()
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo(
            "Selection", "you have selected option " + str(self.radio_var.get())
        )


yourmother = kiloconverter()
