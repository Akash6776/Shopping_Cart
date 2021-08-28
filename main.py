
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image, ImageTk


class ShoppingCart(Frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.adding = True
        self.initUI()


    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))

        def addpress():
            self.adding=not self.adding
            if self.adding==True:
                ar['text'] = "Click to Start \r Removing"
                press()
            else:
                ar['text']="Click to Start \r Adding"
                press()

        def shop(s):
            if(self.adding==True):
                self.shoppinglist.append(s)
            else:
                if s in self.shoppinglist:
                    self.shoppinglist.remove(s)

        self.master.title("Evanz Shopping Store ||"
                          " \r Location: Brgy. Enclaro, Binalbagan, Negros Occidental || "
                          "\r Number: 09121234567")

        ar = tk.Button(self, text="Click to Remove \r Item", bg="green", fg="white", font='Calibri 18 bold', width=15,
                       height=5, command=lambda: [addpress()])
        ar.grid(row=3, column=5)

        exit = tk.Button(self, text="Exit", fg="white", bg="blue", font='Calibri 18 bold',
                         command=self.master.destroy, width=15, height=5)
        exit.grid(row=4, column=5)

        asus = tk.Button(self, command=lambda:[shop("Asus-P25,000"),press()])
        image = ImageTk.PhotoImage(file="asus.gif")
        asus.config(image=image, width=200, height=200, bg="green")
        asus.image = image
        asus.grid(row=2, column=1)

        dell = tk.Button(self, command=lambda:[shop("Dell-P30,000"),press()])
        image = ImageTk.PhotoImage(file="dell-touchscreen.gif")
        dell.config(image=image, width=200, height=200, bg="green")
        dell.image = image
        dell.grid(row=2, column=2)

        headseat = tk.Button(self, command=lambda: [shop("Headseat-P500"),press()])
        image = ImageTk.PhotoImage(file="headseat.gif")
        headseat.config(image=image, width=200, height=200, bg="green")
        headseat.image = image
        headseat.grid(row=2, column=3)

        hp = tk.Button(self, command=lambda:[shop("HP-P45,000"),press()])
        image = ImageTk.PhotoImage(file="hp.gif")
        hp.config(image=image, width=200, height=200, bg="green")
        hp.image = image
        hp.grid(row=2, column=4)

        longsleeve = tk.Button(self, command=lambda: [shop("Long Sleeve-P5,000"), press()])
        image = ImageTk.PhotoImage(file="longsleeve.gif")
        longsleeve.config(image=image, width=200, height=200, bg="green")
        longsleeve.image = image
        longsleeve.grid(row=3, column=1)

        pants = tk.Button(self, command=lambda: [shop("Pants-P4,500"), press()])
        image = ImageTk.PhotoImage(file="pants.gif")
        pants.config(image=image, width=200, height=200, bg="green")
        pants.image = image
        pants.grid(row=3, column=2)

        samsung = tk.Button(self, command=lambda: [shop("Samsung-P15,000"), press()])
        image = ImageTk.PhotoImage(file="samsung.gif")
        samsung.config(image=image, width=200, height=200, bg="green")
        samsung.image = image
        samsung.grid(row=3, column=3)

        luxuryshoes = tk.Button(self, command=lambda: [shop("Luxury Shoes-P15,000"), press()])
        image = ImageTk.PhotoImage(file="shoes1.gif")
        luxuryshoes.config(image=image, width=200, height=200, bg="green")
        luxuryshoes.image = image
        luxuryshoes.grid(row=3, column=4)

        cheapshoes = tk.Button(self, command=lambda: [shop("Cheap Shoes-P1,500"), press()])
        image = ImageTk.PhotoImage(file="shoes2.gif")
        cheapshoes.config(image=image, width=200, height=200, bg="green")
        cheapshoes.image = image
        cheapshoes.grid(row=4, column=1)

        vivo = tk.Button(self, command=lambda: [shop("Vivo-P16,000"), press()])
        image = ImageTk.PhotoImage(file="vivo.gif")
        vivo.config(image=image, width=200, height=200, bg="green")
        vivo.image = image
        vivo.grid(row=4, column=2)

        rolex = tk.Button(self, command=lambda: [shop("Rolex Watch-P12,000"), press()])
        image = ImageTk.PhotoImage(file="watch1.gif")
        rolex.config(image=image, width=200, height=200, bg="green")
        rolex.image = image
        rolex.grid(row=4, column=3)

        applewatch = tk.Button(self, command=lambda: [shop("Apple Watch-P10,000"), press()])
        image = ImageTk.PhotoImage(file="watch2.gif")
        applewatch.config(image=image, width=200, height=200, bg="green")
        applewatch.image = image
        applewatch.grid(row=4, column=4)

        sc = tk.Text(self, height=13, width=30)
        sc.insert(tk.END, getList(self))
        sc.grid(row=2, column=5)

        self.pack()


def getList(self):
    items='Cart Items: \n'
    for item in self.shoppinglist:
        items+= item + "\n"
    return items

def main():
    root = Tk()
    app = ShoppingCart()
    root.configure(background="green")
    root.mainloop()

if __name__ == '__main__':
    main()
