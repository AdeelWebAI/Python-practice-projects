import tkinter
from tkinter import messagebox, ttk, PhotoImage
from openpyxl import load_workbook
root = tkinter.Tk()

root.geometry("500x600")
root.title("Student Registration App")

image_path = PhotoImage(file=r"E:\MY WORKPLACE\Tkinter Tutorial\bg-image.png")
bg_image = tkinter.Label(root, image=image_path)
bg_image.place(relheight=1,relwidth=1)


text_label = tkinter.Label(root, text="Welcome to Student Registration App", font=('calibri', 15))
text_label.pack(pady=20)

file_path = r"E:\MY WORKPLACE\Tkinter Tutorial\testfile.xlsx"
file = load_workbook(file_path)
file_sheet = file["test_Sheet"]


def onClick_name():
    name = name_textbox.get() 
    email = email_textbox.get()
    phone = phone_number_textbox.get()
    branch = choice_dropdown.get()
    agree = agree_value.get()
    # print(agree_value.get())
    # message = f"Name is: {name}\n Email is : {email}\n Phone number is : {phone}"    
    # messagebox.showinfo(message)
    if name and email and phone and branch and (agree==1 or agree==0):
        file_sheet.append([name,email,phone, branch, i])
        file.save(file_path)
        messagebox.showinfo("Status","Data Submited")
    else:
        messagebox.showinfo("Warning","Please fill all the fields")

name_label = tkinter.Label(root, text="Enter Name", font=50)
name_label.pack(anchor=tkinter.W,padx=10)
name_textbox = tkinter.Entry(root, font=50)
name_textbox.pack(anchor=tkinter.W,padx=10)

email_label = tkinter.Label(root, text="Enter Email", font=50)
email_label.pack(anchor=tkinter.W,padx=10)
email_textbox = tkinter.Entry(root, font=50)
email_textbox.pack(anchor=tkinter.W,padx=10)

phone_number_label = tkinter.Label(root, text="Enter Phone Number", font=50)
phone_number_label.pack(anchor=tkinter.W,padx=10)
phone_number_textbox = tkinter.Entry(root, font=50)
phone_number_textbox.pack(anchor=tkinter.W,padx=10)

dropdown_label = tkinter.Label(root, text="Select a branch", font=50)
dropdown_label.pack(anchor=tkinter.W, padx=10)
choices = ["computer science","Software Engineering","Informatoin Technology"]
choice_dropdown = ttk.Combobox(root, values=choices, font=20)
choice_dropdown.pack(anchor=tkinter.W, padx=10)

agree_value = tkinter.IntVar() # uncheck = 0, check = 1
check_value = ttk.Checkbutton(root, text="Do you agree with terms and conditions", variable=agree_value)
check_value.pack(anchor=tkinter.W, padx=10, pady=5)

submit_button = tkinter.Button(root, text="Submit", command=onClick_name, font=50) 
submit_button.pack(anchor=tkinter.W, padx=10, pady=5)

root.mainloop()
