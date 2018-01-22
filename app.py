import Tkinter
import ttk
from Tkinter import *
from ttk import *

class Calculator:

    calc_value = 0.0

    # What's been pressed last
    div_trigger = False
    mtp_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)


    def is_float(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.div_trigger = False
            self.mtp_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())
            
            if value == "/":
                print("/ Pressed")
                self.div_trigger = True
            elif value == "*":
                print("* Pressed")
                self.mtl_trigger = True
            elif value == "+":
                print("+ Pressed")
                self.add_trigger = True
            else:
                print("- Pressed")
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.mtp_trigger or self.div_trigger:
            if self.add_trigger:
                sln = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                sln = self.calc_value - float(self.entry_value.get())
            elif self.mtl_trigger:
                sln = self.calc_value * float(self.entry_value.get())
            else:
                sln = self.calc_value / float(self.entry_value.get())

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, sln)

    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("480x225")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", 
                        font="Serif 15",
                        padding=10)
        style.configure("TEntry", 
                font="Serif 18",
                padding=10)

        self.number_entry = ttk.Entry(root,
                            textvariable=self.entry_value,
                            width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # ------ FIRST ROW -------

        self.button7 = ttk.Button(root,
                            text="7",
                            command=lambda: self.button_press("7")).grid(row=1, column=0)
        self.button8 = ttk.Button(root,
                            text="8",
                            command=lambda: self.button_press("8")).grid(row=1, column=1)
        self.button9 = ttk.Button(root,
                            text="9",
                            command=lambda: self.button_press("9")).grid(row=1, column=2)
        self.button_div = ttk.Button(root,
                            text="/",
                            command=lambda: self.math_button_press("/")).grid(row=1, column=3)

       # ------ SECOND ROW -------

        self.button7 = ttk.Button(root,
                            text="4",
                            command=lambda: self.button_press("4")).grid(row=2, column=0)
        self.button8 = ttk.Button(root,
                            text="5",
                            command=lambda: self.button_press("5")).grid(row=2, column=1)
        self.button9 = ttk.Button(root,
                            text="6",
                            command=lambda: self.button_press("6")).grid(row=2, column=2)
        self.button_div = ttk.Button(root,
                            text="*",
                            command=lambda: self.math_button_press("*")).grid(row=2, column=3)

       # ------ THIRD ROW -------

        self.button7 = ttk.Button(root,
                            text="1",
                            command=lambda: self.button_press("1")).grid(row=3, column=0)
        self.button8 = ttk.Button(root,
                            text="2",
                            command=lambda: self.button_press("2")).grid(row=3, column=1)
        self.button9 = ttk.Button(root,
                            text="3",
                            command=lambda: self.button_press("3")).grid(row=3, column=2)
        self.button_div = ttk.Button(root,
                            text="+",
                            command=lambda: self.math_button_press("+")).grid(row=3, column=3)

       # ------ FOURTH ROW -------

        self.button7 = ttk.Button(root,
                            text="AC",
                            command=lambda: self.button_press("AC")).grid(row=4, column=0)
        self.button8 = ttk.Button(root,
                            text="0",
                            command=lambda: self.button_press("0")).grid(row=4, column=1)
        self.button9 = ttk.Button(root,
                            text="=",
                            command=lambda: self.equal_button_press()).grid(row=4, column=2)
        self.button_div = ttk.Button(root,
                            text="-",
                            command=lambda: self.math_button_press("-")).grid(row=4, column=3)

root = Tk()

calc = Calculator(root)

root.mainloop()
        