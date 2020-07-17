import numpy as np
import tkinter as tk

class Board():
    def __init__(self):
        self.board = tk.Tk()
        for i in range(30):
            for j in range(30):
                self.frame = tk.Frame(master=self.board, relief=tk.RAISED, borderwidth= 2)
                self.frame.grid(column = j, row = i)
                self.button = tk.Button(master=self.frame, bg="white")
                self.button.grid(column = j, row = i)
        
        self.board.mainloop()

    def make_black(self):
        self.button.configure(bg = "black")

board = Board()


