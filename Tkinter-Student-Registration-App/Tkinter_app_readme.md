# 🎓 Student Registration App

A simple desktop-based **Student Registration Application** built using **Python Tkinter** and **OpenPyXL**.

This application allows users to enter student details through a graphical interface and store the data directly into an Excel file.

---

## 🚀 Features

* 🖼 Background image support
* 📝 Student registration form
* 📧 Email and phone input fields
* 🎓 Branch selection using dropdown (Combobox)
* ✅ Terms & conditions checkbox
* 💾 Automatic data storage into Excel file
* 📦 Simple and beginner-friendly code structure

---

## 🛠 Technologies Used

* **Python 3.x**
* **Tkinter** (GUI)
* **ttk** (Styled widgets)
* **OpenPyXL** (Excel file handling)

---

## 📂 Project Structure

```
Student-Registration-App/
│
├── main.py
├── bg-image.png
├── testfile.xlsx
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository (or download the files)

```bash
copy past this code in your local file
```

### 2️⃣ Install required dependency

```bash
pip install openpyxl
```

Tkinter comes pre-installed with Python (no need to install separately).

---

## ▶️ How to Run

```bash
python tkinter_app.py
```

---

## 🧾 How It Works

1. User enters:

   * Name
   * Email
   * Phone Number
   * Selects a Branch
   * Agrees to terms and conditions

2. When the **Submit** button is clicked:

   * Data is validated.
   * If all fields are filled, the data is appended to `testfile.xlsx`.
   * A success message is displayed.
   * If fields are missing, a warning message appears.

---

## 📌 Requirements

* Python 3.8+
* Excel file (`testfile.xlsx`) must contain a sheet named:

```
test_Sheet
```

---

## ⚠️ Important Notes

* Ensure the Excel file path is correct in the script.
* Make sure the background image path is correct.
* The Excel file must not be open while submitting data (or it may cause a save error).

---

## 🎯 Future Improvements

* Add email validation
* Add phone number format validation
* Clear form after submission
* Add error handling for file issues
* Convert to database-based system (SQLite / PostgreSQL)

---

## 👨‍💻 Author

Developed by **Muhammad Adeel**

---

✨ This project is great for beginners learning:
