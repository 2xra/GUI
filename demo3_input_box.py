import tkinter
import tkinter.messagebox


class kiloconverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.promptlabel = tkinter.Label(self.top_frame, text="how many km?")

        self.promptlabel.pack(side="left")

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.kilo_entry.pack(side="left")

        self.calcbutton = tkinter.Button(
            self.main_window, text="convert", command=self.convert
        )
        self.quitbutton = tkinter.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )
        self.top_frame.pack(side="top")
        self.quitbutton.pack(side="right")
        self.calcbutton.pack(side="left")

        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214, 2)
        tkinter.messagebox.showinfo(
            "results", str(kilo) + " km is equal to " + str(miles) + " miles"
        )


yourmother = kiloconverter()
