import tkinter as tk
from tkinter import messagebox

def sum(a, b, c):
    return a + b + c

def gboard(xState, zState):
    return f"{xState[0]} | {xState[1]} | {xState[2]}\n--|---|--\n{xState[3]} | {xState[4]} | {xState[5]}\n--|---|--\n{xState[6]} | {xState[7]} | {xState[8]}"

# Check if any person is the winner
def checkwinner(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return "X"
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return "O"
    return None

# Check if the gboard is full
def is_board_full(xState, zState):
    return all(x or z for x, z in zip(xState, zState))

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        self.buttons = []
        self.xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1
        
        for i in range(9):
            btn = tk.Button(self.window, text="", font=('Arial', 20), width=4, height=2,
                            command=lambda idx=i: self.on_button_click(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)
        
    def on_button_click(self, idx):
        if self.xState[idx] == 0 and self.zState[idx] == 0:
            if self.turn == 1:
                self.xState[idx] = 1
                self.buttons[idx].config(text="X")
            else:
                self.zState[idx] = 1
                self.buttons[idx].config(text="O")
                
            winner = checkwinner(self.xState, self.zState)
            if winner:
                messagebox.showinfo("Game Over", f"{winner} won the game!")
                self.window.destroy()
            elif is_board_full(self.xState, self.zState):
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.window.destroy()
            else:
                self.turn = 1 - self.turn
                
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()