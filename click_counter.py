from tkinter import *


class Clicker():
    def __init__(self):
        self.counter = 0

    def click(self):
        self.counter += 1
        pass

    def start(self):
        window1 = Tk()
        window1.geometry("400x300")

        placeholder = Label(window1, text=" ", height=5).pack()
        button = Button(window1, text="Click Me!", height=10, width=20, command=self.click).pack(padx=100)
        print(self.counter)

        window1.mainloop()


clicker = Clicker()
clicker.start()
