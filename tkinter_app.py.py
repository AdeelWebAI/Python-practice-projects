import tkinter
from tkinter import messagebox, ttk
from openpyxl import load_workbook
root = tkinter.Tk()
file_path = r"E:\MY WORKPLACE\Tkinter Tutorial\testfile.xlsx"
file = load_workbook(file_path)
file_sheet = file["test_Sheet"]


def onClick_name():
    name = name_textbox.get()
    email = email_textbox.get()
    phone = phone_number_textbox.get()
    branch = choice_dropdown.get()
    # message = f"Name is: {name}\n Email is : {email}\n Phone number is : {phone}"    
    # messagebox.showinfo(message)
    if name and email and phone and branch:
        file_sheet.append([name,email,phone, branch])
        file.save(file_path)
        messagebox.showinfo("Status","Data Submited")
    else:
        messagebox.showinfo("Warning","Please fill all the fields")
root.geometry("300x400")

root.configure(bg="green")

root.title("Student Registration form")

name_label = tkinter.Label(root, text="Enter Name")
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox = tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W,padx=10)

email_label = tkinter.Label(root, text="Enter Email")
email_label.pack(anchor=tkinter.W,padx=10)
email_textbox = tkinter.Entry(root)
email_textbox.pack(anchor=tkinter.W,padx=10)

phone_number_label = tkinter.Label(root, text="Enter Phone Number")
phone_number_label.pack(anchor=tkinter.W,padx=10)
phone_number_textbox = tkinter.Entry(root)
phone_number_textbox.pack(anchor=tkinter.W,padx=10)

dropdown_label = tkinter.Label(root, text="Select a branch")
dropdown_label.pack(anchor=tkinter.W, padx=10)
choices = ["computer science","Software Engineering","Informatoin Technology"]
choice_dropdown = ttk.Combobox(root, values=choices)
choice_dropdown.pack(anchor=tkinter.W, padx=10)

submit_button = tkinter.Button(root, text="Submit", command=onClick_name) 
submit_button.pack(anchor=tkinter.W, padx=50)

root.mainloop()