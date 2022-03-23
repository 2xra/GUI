import tkinter
import tkinter.messagebox

"""Step 1:tick boxes
Step 2:????
Step 3: PIZZA

is it ugly?
Yes
Does it have all the things?
I think.

I apologize that this is very unprofessional looking,
I mainly just hacked together previous code from assignments
because I realized this was due today at 5:00 and had plans already.

I solemnly swear to never let code like this get into a production system that another person will touch.

-Reese
"""
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("600x600")
        self.main_window.title("Baylor Pizza is the Pizza for Me!")
        self.fontchoice = ("Comic Sans MS", 12)
        
        self.buttonbgcolor = "#154734"
        self.textcolor = "#FFB81C"
        self.main_window.configure(bg=self.buttonbgcolor)
        self.top_frame = tkinter.Frame(self.main_window,bg=self.buttonbgcolor,)
        self.bottom_frame = tkinter.Frame(self.main_window,bg=self.buttonbgcolor,)
        self.radio_var = tkinter.IntVar()
        self.cost_var = tkinter.StringVar()
        self.costlabel = tkinter.Label(self.bottom_frame, textvariable=self.cost_var,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,)
        self.costlabel.pack()
        self.promptlabel = tkinter.Label(self.top_frame, text="What's your name?",
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,)

        self.promptlabel.pack(side="top")

        self.customer_name = tkinter.Entry(self.top_frame, width=10,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,)

        self.customer_name.pack(side="top")

        # create three int variables to use with the checkbuttons
        self.rb1 = tkinter.Radiobutton(
            self.top_frame, text="Thicc Crust $5", variable=self.radio_var, value=5,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )

        self.rb2 = tkinter.Radiobutton(
            self.top_frame, text="Thin Crust $4", variable=self.radio_var, value=4,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )

        self.rb3 = tkinter.Radiobutton(
            self.top_frame, text="No Crust?(What does this mean?) $1", variable=self.radio_var, value=1,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )

        # sets default button
        self.rb3.select()


        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.pepperoni1 = tkinter.IntVar()
        self.ham2 = tkinter.IntVar()
        self.pineapple3 = tkinter.IntVar()

        self.pepperoni1.set(0)
        self.ham2.set(1)
        self.pineapple3.set(1)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Pepperoni $1", variable=self.pepperoni1,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )

        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Ham $2", variable=self.ham2,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Pineapple $3", variable=self.pineapple3,command=self.costcalc,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.mybutton = tkinter.Button(
            self.main_window, text="Checkout ->", command=self.placeorder,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.quitbutton = tkinter.Button(
            self.main_window, text="I don't want pizza", command=self.getout,
            bg=self.buttonbgcolor,
            fg=self.textcolor,
            font=self.fontchoice,
        )
        self.quitbutton.pack(side="left")
        self.mybutton.pack(side="right")

        self.bottom_frame.pack(side="bottom")
        self.top_frame.pack(side="top")
        self.costcalc()
        tkinter.mainloop()

    def costcalc(self):
        cost=0
        cost += self.radio_var.get()
        cost += self.pepperoni1.get()+self.ham2.get()*2+self.pineapple3.get()*3
        self.cost_var.set('Your total is: $'+str(cost))

    def getout(self):
        tkinter.messagebox.showinfo('Great.', "Well pizza doesn't want you.")
        self.main_window.destroy()

    def placeorder(self):
        custname = self.customer_name.get()
        self.costcalc()
        self.message ="Thank you, "+custname+", for ordering. \nYou have selected:\n"

        if self.pepperoni1.get() == 1:
            self.message += "Pepperoni $1\n"

        if self.ham2.get() == 1:
            self.message += "Ham $2\n"

        if self.pineapple3.get() == 1:

            self.message += "Pineapple $3\n"

        if self.radio_var.get() == 5:
            self.message += 'Thicc crust $5'
        
        if self.radio_var.get() == 4:
            self.message += 'Thin crust $4'
        
        if self.radio_var.get() == 1:
            self.message += 'Air.... $1'

        self.message += '\n'+self.cost_var.get()
        tkinter.messagebox.showinfo('Order Placed', self.message)


yourmother = MyGUI()
