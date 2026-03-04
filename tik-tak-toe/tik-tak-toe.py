import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False


def check_winner():
    global winner

    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],     
        [0,4,8], [2,4,6]               
    ]

    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            
            for i in combo:
                buttons[i].config(bg="green")

            winner = True
            label.config(text=f"Player {buttons[combo[0]]['text']} Wins!")
            disable_buttons()
            return

    if all(button["text"] != "" for button in buttons) and not winner:
        label.config(text="Match Tie!")
        winner = True
        disable_buttons()


def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s Turn")


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()

        if not winner:
            toggle_player()


def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s Turn")

    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")


buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 40),
                       width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

label = tk.Label(root, text=f"Player {current_player}'s Turn",
                 font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3, pady=10)

restart_btn = tk.Button(root, text="Restart Game",
                        font=("Arial", 14),
                        command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()