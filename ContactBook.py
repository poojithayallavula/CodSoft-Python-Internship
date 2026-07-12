from tkinter import *
from tkinter import messagebox

contacts = []
selected_index = None

# ------------------ Functions ------------------

def clear_fields():
    global selected_index
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    selected_index = None

def display_contacts(contact_list=None):
    for widget in display_frame.winfo_children():
        widget.destroy()

    if contact_list is None:
        contact_list = contacts

    for index, contact in enumerate(contact_list):

        card = Frame(display_frame, bg="#1f5c8d", bd=2, relief=RIDGE)
        card.pack(fill=X, padx=10, pady=5)

        Label(card, text="👤 " + contact["name"],
              bg="#1f5c8d", fg="white",
              font=("Arial",12,"bold")).pack(anchor="w", padx=10, pady=(5,0))

        Label(card, text="📞 " + contact["phone"],
              bg="#1f5c8d", fg="white",
              font=("Arial",10)).pack(anchor="w", padx=10)

        Label(card, text="✉ " + contact["email"],
              bg="#1f5c8d", fg="white",
              font=("Arial",10)).pack(anchor="w", padx=10)

        btn_frame = Frame(card, bg="#1f5c8d")
        btn_frame.pack(anchor="e", padx=10, pady=5)

        Button(btn_frame,text="Edit",
               command=lambda i=index: edit_contact(i),
               bg="orange").pack(side=LEFT,padx=5)

        Button(btn_frame,text="Delete",
               command=lambda i=index: delete_contact(i),
               bg="red",fg="white").pack(side=LEFT)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name=="" or phone=="" or email=="":
        messagebox.showerror("Error","Fill all fields")
        return

    contacts.append({
        "name":name,
        "phone":phone,
        "email":email
    })

    clear_fields()
    display_contacts()

def edit_contact(index):
    global selected_index
    selected_index=index

    clear_fields()

    name_entry.insert(0,contacts[index]["name"])
    phone_entry.insert(0,contacts[index]["phone"])
    email_entry.insert(0,contacts[index]["email"])

    selected_index=index

def update_contact():
    global selected_index

    if selected_index is None:
        messagebox.showerror("Error","Select a contact")
        return

    contacts[selected_index]={
        "name":name_entry.get(),
        "phone":phone_entry.get(),
        "email":email_entry.get()
    }

    clear_fields()
    display_contacts()

def delete_contact(index):
    del contacts[index]
    display_contacts()

def search_contact():
    keyword=search_entry.get().lower()

    result=[]

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            result.append(contact)

    display_contacts(result)

def show_all():
    search_entry.delete(0,END)
    display_contacts()

# ---------------- GUI ----------------

root=Tk()
root.title("Contact Book")
root.geometry("700x650")
root.configure(bg="#d9edf7")

title=Label(root,
            text="CONTACT BOOK",
            font=("Arial",20,"bold"),
            bg="#d9edf7")
title.pack(pady=10)

form=Frame(root,bg="#d9edf7")
form.pack()

Label(form,text="Name",bg="#d9edf7").grid(row=0,column=0,padx=5,pady=5)

name_entry=Entry(form,width=35)
name_entry.grid(row=0,column=1)

Label(form,text="Phone",bg="#d9edf7").grid(row=1,column=0,padx=5,pady=5)

phone_entry=Entry(form,width=35)
phone_entry.grid(row=1,column=1)

Label(form,text="Email",bg="#d9edf7").grid(row=2,column=0,padx=5,pady=5)

email_entry=Entry(form,width=35)
email_entry.grid(row=2,column=1)

button_frame=Frame(root,bg="#d9edf7")
button_frame.pack(pady=10)

Button(button_frame,
       text="Add Contact",
       bg="green",
       fg="white",
       width=15,
       command=add_contact).grid(row=0,column=0,padx=5)

Button(button_frame,
       text="Update",
       bg="orange",
       width=15,
       command=update_contact).grid(row=0,column=1,padx=5)

Button(button_frame,
       text="Clear",
       width=15,
       command=clear_fields).grid(row=0,column=2,padx=5)

search_frame=Frame(root,bg="#d9edf7")
search_frame.pack(pady=10)

search_entry=Entry(search_frame,width=30)
search_entry.pack(side=LEFT,padx=5)

Button(search_frame,
       text="Search",
       command=search_contact).pack(side=LEFT,padx=5)

Button(search_frame,
       text="Show All",
       command=show_all).pack(side=LEFT)

display_frame=Frame(root,bg="#d9edf7")
display_frame.pack(fill=BOTH,expand=True)

display_contacts()

root.mainloop()