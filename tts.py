import tkinter as tk
import pyttex3

class Widget():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TTS")
        self.root.resizable(0,0)
        self.root.configure(background="pink")
        self.label = tk.Label(self.root, bg="pink", fg="brown", font="Arial 30 bold", text="What you want me to speak?" )
        self.label.pack()
        self.entry = tk.Entry(self.root, width=35, font="Arial 25")
        self.entry.pack()
        self.button = tk.Button(self.root, bg="pink", fg="brown", font="Arial 25 bold", text="SPEAK")
        self.button.pack()
        self.root.mainloop()

if __name__ == "__main__":
    temp = Widget()