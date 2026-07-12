import customtkinter as ctk
import random
import string

# -------------------- Window -------------------- #

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Generator")
app.geometry("550x600")
app.resizable(False, False)

# -------------------- Title -------------------- #

title = ctk.CTkLabel(
    app,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 26, "bold")
)
title.pack(pady=20)

# -------------------- Password Length -------------------- #

length_label = ctk.CTkLabel(
    app,
    text="Password Length",
    font=("Arial",16)
)
length_label.pack()

length_entry = ctk.CTkEntry(
    app,
    width=150,
    justify="center",
    font=("Arial",18)
)
length_entry.pack(pady=10)

# -------------------- Options -------------------- #

uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

options = ctk.CTkFrame(app)
options.pack(pady=15)

ctk.CTkCheckBox(
    options,
    text="Uppercase (A-Z)",
    variable=uppercase_var
).pack(anchor="w", padx=20, pady=5)

ctk.CTkCheckBox(
    options,
    text="Lowercase (a-z)",
    variable=lowercase_var
).pack(anchor="w", padx=20, pady=5)

ctk.CTkCheckBox(
    options,
    text="Numbers (0-9)",
    variable=numbers_var
).pack(anchor="w", padx=20, pady=5)

ctk.CTkCheckBox(
    options,
    text="Special Characters (!@#$%^&*)",
    variable=symbols_var
).pack(anchor="w", padx=20, pady=5)

# -------------------- Output -------------------- #

password_box = ctk.CTkEntry(
    app,
    width=420,
    height=45,
    font=("Arial",18),
    justify="center"
)
password_box.pack(pady=20)

strength_label = ctk.CTkLabel(
    app,
    text="Password Strength: -",
    font=("Arial",16)
)
strength_label.pack()

# Status Label
status_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial",14),
    text_color="lightgreen"
)
status_label.pack(pady=5)

# -------------------- Generate Password -------------------- #

def generate_password():

    password_box.delete(0, "end")

    try:
        length = int(length_entry.get())

        if length <= 0:
            password_box.insert(0, "Enter valid length")
            return

    except ValueError:
        password_box.insert(0, "Invalid Length")
        return

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if characters == "":
        password_box.insert(0, "Select at least one option")
        return

    password = "".join(random.choice(characters) for _ in range(length))

    password_box.insert(0, password)

    # Clear previous status message
    status_label.configure(text="")

    # Password Strength
    if length < 8:
        strength = "Weak"
        color = "red"
    elif length < 12:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "lightgreen"

    strength_label.configure(
        text=f"Password Strength: {strength}",
        text_color=color
    )
    # -------------------- Copy Password -------------------- #

def copy_password():

    password = password_box.get().strip()

    # Check if there is a valid password
    if password == "" or password in (
        "Invalid Length",
        "Enter valid length",
        "Select at least one option"
    ):
        status_label.configure(
            text="⚠ No password to copy!",
            text_color="red"
        )
        return

    # Copy password to clipboard
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()

    # Show success message
    status_label.configure(
        text="✅ Password copied successfully!",
        text_color="lightgreen"
    )

# -------------------- Buttons -------------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

generate_btn = ctk.CTkButton(
    button_frame,
    text="Generate Password",
    width=180,
    height=45,
    command=generate_password
)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = ctk.CTkButton(
    button_frame,
    text="Copy Password",
    width=180,
    height=45,
    fg_color="green",
    hover_color="darkgreen",
    command=copy_password
)
copy_btn.grid(row=0, column=1, padx=10)

# -------------------- Footer -------------------- #

footer = ctk.CTkLabel(
    app,
    text="Developed using Python & CustomTkinter",
    font=("Arial", 13)
)
footer.pack(side="bottom", pady=15)

# -------------------- Run Application -------------------- #

app.mainloop()