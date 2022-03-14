import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("100x150")
        self.label1 = tkinter.Label(self.main_window, text="Hello World!")

        self.label2 = tkinter.Label(self.main_window, text="This is it chief.")

        self.label1.pack(side="bottom")
        self.label2.pack(side="top")

        tkinter.mainloop()


ya = MyGUI()

print("moving on....")
