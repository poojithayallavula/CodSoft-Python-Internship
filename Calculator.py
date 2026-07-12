import customtkinter as ctk
import math

# ---------------- Window ---------------- #

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Scientific Calculator")
app.geometry("420x620")
app.resizable(False, False)

expression = ""

# ---------------- Functions ---------------- #

def press(value):
    global expression
    expression += str(value)
    display.delete(0, "end")
    display.insert(0, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, "end")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, "end")
        display.insert(0, result)
        expression = result
    except:
        display.delete(0, "end")
        display.insert(0, "Error")
        expression = ""

def square():
    global expression
    try:
        result = eval(display.get())
        result = result ** 2
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def sqrt():
    global expression
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def sin():
    global expression
    try:
        result = math.sin(math.radians(float(display.get())))
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def cos():
    global expression
    try:
        result = math.cos(math.radians(float(display.get())))
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def tan():
    global expression
    try:
        result = math.tan(math.radians(float(display.get())))
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def log():
    global expression
    try:
        result = math.log10(float(display.get()))
        display.delete(0, "end")
        display.insert(0, result)
        expression = str(result)
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

def pi():
    global expression
    display.delete(0, "end")
    display.insert(0, math.pi)
    expression = str(math.pi)

# ---------------- Title ---------------- #

title = ctk.CTkLabel(
    app,
    text="SCIENTIFIC CALCULATOR",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

# ---------------- Display ---------------- #

display = ctk.CTkEntry(
    app,
    width=360,
    height=60,
    font=("Arial", 24),
    justify="right"
)
display.pack(pady=10)

# ---------------- Buttons ---------------- #

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
]

for text,row,col in buttons:

    if text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: press(t)

    btn = ctk.CTkButton(
        frame,
        text=text,
        width=75,
        height=55,
        command=cmd
    )

    btn.grid(row=row,column=col,padx=5,pady=5)

# Scientific Buttons

science = ctk.CTkFrame(app)
science.pack(pady=10)

ctk.CTkButton(science,text="√",width=75,command=sqrt).grid(row=0,column=0,padx=5,pady=5)
ctk.CTkButton(science,text="x²",width=75,command=square).grid(row=0,column=1,padx=5,pady=5)
ctk.CTkButton(science,text="sin",width=75,command=sin).grid(row=0,column=2,padx=5,pady=5)
ctk.CTkButton(science,text="cos",width=75,command=cos).grid(row=0,column=3,padx=5,pady=5)

ctk.CTkButton(science,text="tan",width=75,command=tan).grid(row=1,column=0,padx=5,pady=5)
ctk.CTkButton(science,text="log",width=75,command=log).grid(row=1,column=1,padx=5,pady=5)
ctk.CTkButton(science,text="π",width=75,command=pi).grid(row=1,column=2,padx=5,pady=5)
ctk.CTkButton(science,text="C",width=75,fg_color="red",
              hover_color="darkred",
              command=clear).grid(row=1,column=3,padx=5,pady=5)

# ---------------- Footer ---------------- #

footer = ctk.CTkLabel(
    app,
    text="Developed using Python & CustomTkinter",
    font=("Arial",12)
)
footer.pack(side="bottom", pady=10)

app.mainloop()