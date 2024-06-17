
from tkinter import *
from tkinter import ttk
import random


def grid_configure(window, rows, cols):
    for i in range(rows):
        window.grid_rowconfigure(i, weight=1)
    for j in range(cols):
        window.grid_columnconfigure(j, weight=1)


def clear_window():
    for widget in frm.winfo_children():
        widget.destroy()


def button_click(button, position):
    global x_player
    if button['text'] == "":
        if x_player:
            button['text'] = "X"
            combination[position] = "X"
        else:
            button['text'] = "O"
            combination[position] = "O"
        x_player = not x_player
        win_condition(combination)


def win_condition(w):
    if (w[0] == "X" and w[1] == "X" and w[2] == "X") or (w[3] == "X" and w[4] == "X" and w[5] == "X") or (w[6] == "X" and w[7] == "X" and w[8] == "X") or (w[0] == "X" and w[3] == "X" and w[6] == "X") or (w[1] == "X" and w[4] == "X" and w[7] == "X") or (w[2] == "X" and w[5] == "X" and w[8] == "X") or (w[0] == "X" and w[4] == "X" and w[8] == "X") or (w[2] == "X" and w[4] == "X" and w[6] == "X"):
        win_screen("X", game)
    elif (w[0] == "O" and w[1] == "O" and w[2] == "O") or (w[3] == "O" and w[4] == "O" and w[5] == "O") or (w[6] == "O" and w[7] == "O" and w[8] == "O") or (w[0] == "O" and w[3] == "O" and w[6] == "O") or (w[1] == "O" and w[4] == "O" and w[7] == "O") or (w[2] == "O" and w[5] == "O" and w[8] == "O") or (w[0] == "O" and w[4] == "O" and w[8] == "O") or (w[2] == "O" and w[4] == "O" and w[6] == "O"):
        win_screen("O", game)
    elif all(value != "" for value in w):
        tie_screen(game)
    else:
        pass

def win_screen(player, game):
    global combination
    combination = ["", "", "", "", "", "", "", "", ""]
    clear_window()
    ttk.Label(frm, text=f"Player {player} Wins", font=("Arial", 18), anchor="center").grid(column=0, row=0)
    ttk.Button(frm, text="Restart", command=game, style="Large.TButton").grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy, style="Large.TButton").grid(column=0, row=2)

def tie_screen(game):
    global combination
    combination = ["", "", "", "", "", "", "", "", ""]
    clear_window()
    ttk.Label(frm, text=f"Its a Tie", font=("Arial", 18), anchor="center").grid(column=0, row=0)
    ttk.Button(frm, text="Restart", command=game, style="Large.TButton").grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy, style="Large.TButton").grid(column=0, row=2)


def tic_tac_toe_grid():
    button1 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button1, 0))
    button1.grid(row=1, column=0, padx=5, pady=5, sticky=(N, S, E, W))
    button2 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button2, 1))
    button2.grid(row=1, column=1, padx=5, pady=5, sticky=(N, S, E, W))
    button3 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button3, 2))
    button3.grid(row=1, column=2, padx=5, pady=5, sticky=(N, S, E, W))

    button4 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button4, 3))
    button4.grid(row=2, column=0, padx=5, pady=5, sticky=(N, S, E, W))
    button5 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button5, 4))
    button5.grid(row=2, column=1, padx=5, pady=5, sticky=(N, S, E, W))
    button6 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button6, 5))
    button6.grid(row=2, column=2, padx=5, pady=5, sticky=(N, S, E, W))

    button7 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button7, 6))
    button7.grid(row=3, column=0, padx=5, pady=5, sticky=(N, S, E, W))
    button8 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button8, 7))
    button8.grid(row=3, column=1, padx=5, pady=5, sticky=(N, S, E, W))
    button9 = ttk.Button(frm, text="", style="Large.TButton", command=lambda: button_click(button9, 8))
    button9.grid(row=3, column=2, padx=5, pady=5, sticky=(N, S, E, W))


def PVP():
    global game
    game = PVP
    clear_window()
    root.title("Player Vs Player")
    if x_player:
        ttk.Label(frm, text="Player X starts first", font=("Arial", 18), anchor="center").grid(column=1, row=0)
    else:
        ttk.Label(frm, text="Player O start first", font=("Arial", 18), anchor="center").grid(column=1, row=0)
    tic_tac_toe_grid()
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)


def PVA():
    global game
    game = PVA
    clear_window() 
    root.title("Player Vs AI")
    if x_player:
        ttk.Label(frm, text="Player X starts first", font=("Arial", 18), anchor="center").grid(column=1, row=0)
    else:
        ttk.Label(frm, text="Player O start first", font=("Arial", 18), anchor="center").grid(column=1, row=0)
    tic_tac_toe_grid()
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)



def main():
    global root
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("600x600")
    grid_configure(root, 1, 1)

    global frm
    frm = ttk.Frame(root, padding=10)
    frm.grid(sticky=(N, S, E, W))
    grid_configure(frm, 4, 1)

    global x_player
    x_player = True

    global combination
    combination = ["", "", "", "", "", "", "", "", ""]


    button_style = ttk.Style()
    button_style.configure("Large.TButton", font=("Arial", 16), padding=20)

    ttk.Label(frm, text="Tic Tac Toe", font=("Arial", 24), anchor="center").grid(column=0, row=0, sticky=(N, S, E, W))
    ttk.Button(frm, text="Player Vs Player", command=PVP, style="Large.TButton").grid(column=0, row=1)
    ttk.Button(frm, text="Player Vs AI", command=PVA, style="Large.TButton").grid(column=0, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy, style="Large.TButton").grid(column=0, row=3)
    
    root.mainloop()



if __name__ == "__main__":
    main()
