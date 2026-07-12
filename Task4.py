import customtkinter as ctk
import random

# -------------------- Window -------------------- #

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Rock Paper Scissors")
app.geometry("650x650")
app.resizable(False, False)

# -------------------- Variables -------------------- #

user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# -------------------- Title -------------------- #

title = ctk.CTkLabel(
    app,
    text="✊ ROCK • PAPER • SCISSORS ✌",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# -------------------- Score Board -------------------- #

score_frame = ctk.CTkFrame(app)
score_frame.pack(pady=10)

user_score_label = ctk.CTkLabel(
    score_frame,
    text="👤 Your Score : 0",
    font=("Arial",18,"bold")
)
user_score_label.grid(row=0,column=0,padx=40,pady=10)

computer_score_label = ctk.CTkLabel(
    score_frame,
    text="🤖 Computer Score : 0",
    font=("Arial",18,"bold")
)
computer_score_label.grid(row=0,column=1,padx=40,pady=10)

# -------------------- Display -------------------- #

display_frame = ctk.CTkFrame(app)
display_frame.pack(pady=20)

user_choice_label = ctk.CTkLabel(
    display_frame,
    text="Your Choice : -",
    font=("Arial",18)
)
user_choice_label.pack(pady=10)

computer_choice_label = ctk.CTkLabel(
    display_frame,
    text="Computer Choice : -",
    font=("Arial",18)
)
computer_choice_label.pack(pady=10)

result_label = ctk.CTkLabel(
    display_frame,
    text="Choose Rock, Paper or Scissors",
    font=("Arial",20,"bold"),
    text_color="yellow"
)
result_label.pack(pady=20)

# -------------------- Game Function -------------------- #

def play(user_choice):

    global user_score
    global computer_score

    computer_choice = random.choice(choices)

    user_choice_label.configure(
        text=f"Your Choice : {user_choice}"
    )

    computer_choice_label.configure(
        text=f"Computer Choice : {computer_choice}"
    )

    if user_choice == computer_choice:

        result = "🤝 It's a Tie!"
        color = "yellow"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):

        user_score += 1

        result = "🎉 You Win!"
        color = "lightgreen"

    else:

        computer_score += 1

        result = "😔 Computer Wins!"
        color = "red"

    result_label.configure(
        text=result,
        text_color=color
    )

    user_score_label.configure(
        text=f"👤 Your Score : {user_score}"
    )

    computer_score_label.configure(
        text=f"🤖 Computer Score : {computer_score}"
    )
    # -------------------- Buttons -------------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

rock_button = ctk.CTkButton(
    button_frame,
    text="✊ Rock",
    width=160,
    height=50,
    font=("Arial",16,"bold"),
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = ctk.CTkButton(
    button_frame,
    text="✋ Paper",
    width=160,
    height=50,
    font=("Arial",16,"bold"),
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = ctk.CTkButton(
    button_frame,
    text="✌ Scissors",
    width=160,
    height=50,
    font=("Arial",16,"bold"),
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# -------------------- Functions -------------------- #

def play_again():

    user_choice_label.configure(
        text="Your Choice : -"
    )

    computer_choice_label.configure(
        text="Computer Choice : -"
    )

    result_label.configure(
        text="Choose Rock, Paper or Scissors",
        text_color="yellow"
    )


def reset_game():

    global user_score
    global computer_score

    user_score = 0
    computer_score = 0

    user_score_label.configure(
        text="👤 Your Score : 0"
    )

    computer_score_label.configure(
        text="🤖 Computer Score : 0"
    )

    play_again()


# -------------------- Control Buttons -------------------- #

control_frame = ctk.CTkFrame(app)
control_frame.pack(pady=20)

play_again_btn = ctk.CTkButton(
    control_frame,
    text="▶ Play Again",
    width=180,
    height=45,
    fg_color="green",
    hover_color="darkgreen",
    command=play_again
)
play_again_btn.grid(row=0, column=0, padx=15)

reset_btn = ctk.CTkButton(
    control_frame,
    text="🔄 Reset Game",
    width=180,
    height=45,
    fg_color="red",
    hover_color="darkred",
    command=reset_game
)
reset_btn.grid(row=0, column=1, padx=15)

# -------------------- Footer -------------------- #

footer = ctk.CTkLabel(
    app,
    text="Developed using Python & CustomTkinter",
    font=("Arial",13)
)
footer.pack(side="bottom", pady=15)

# -------------------- Run Application -------------------- #

app.mainloop()