import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Student Management System")
root.geometry("800x500")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    course TEXT
)""")
conn.commit()

def fetch_students():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, values=row)

def add_student():
    if name_var.get() == "" or age_var.get() == "" or gender_var.get() == "" or course_var.get() == "":
        messagebox.showerror("Error", "All fields are required")
        return
    cursor.execute("INSERT INTO students (name, age, gender, course) VALUES (?, ?, ?, ?)",
                   (name_var.get(), age_var.get(), gender_var.get(), course_var.get()))
    conn.commit()
    fetch_students()
    clear_fields()

def update_student():
    if id_var.get() == "":
        messagebox.showerror("Error", "Please select a student to update")
        return
    cursor.execute("UPDATE students SET name=?, age=?, gender=?, course=? WHERE id=?",
                   (name_var.get(), age_var.get(), gender_var.get(), course_var.get(), id_var.get()))
    conn.commit()
    fetch_students()
    clear_fields()

def delete_student():
    if id_var.get() == "":
        messagebox.showerror("Error", "Please select a student to delete")
        return
    cursor.execute("DELETE FROM students WHERE id=?", (id_var.get(),))
    conn.commit()
    fetch_students()
    clear_fields()

def clear_fields():
    id_var.set("")
    name_var.set("")
    age_var.set("")
    gender_var.set("")
    course_var.set("")

def on_tree_select(event):
    selected = tree.focus()
    values = tree.item(selected, 'values')
    if values:
        id_var.set(values[0])
        name_var.set(values[1])
        age_var.set(values[2])
        gender_var.set(values[3])
        course_var.set(values[4])

id_var = StringVar()
name_var = StringVar()
age_var = StringVar()
gender_var = StringVar()
course_var = StringVar()

form_frame = Frame(root, padx=10, pady=10)
form_frame.pack(side=TOP, fill=X)

Label(form_frame, text="Name").grid(row=0, column=0)
Entry(form_frame, textvariable=name_var).grid(row=0, column=1)

Label(form_frame, text="Age").grid(row=0, column=2)
Entry(form_frame, textvariable=age_var).grid(row=0, column=3)

Label(form_frame, text="Gender").grid(row=1, column=0)
Entry(form_frame, textvariable=gender_var).grid(row=1, column=1)

Label(form_frame, text="Course").grid(row=1, column=2)
Entry(form_frame, textvariable=course_var).grid(row=1, column=3)

Button(form_frame, text="Add", command=add_student, bg="green", fg="white", width=12).grid(row=2, column=0, pady=10)
Button(form_frame, text="Update", command=update_student, bg="blue", fg="white", width=12).grid(row=2, column=1)
Button(form_frame, text="Delete", command=delete_student, bg="red", fg="white", width=12).grid(row=2, column=2)
Button(form_frame, text="Clear", command=clear_fields, width=12).grid(row=2, column=3)

tree_frame = Frame(root)
tree_frame.pack(fill=BOTH, expand=1)

scroll_y = Scrollbar(tree_frame, orient=VERTICAL)
tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "Gender", "Course"), yscrollcommand=scroll_y.set)
scroll_y.config(command=tree.yview)
scroll_y.pack(side=RIGHT, fill=Y)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Gender", text="Gender")
tree.heading("Course", text="Course")
tree['show'] = 'headings'
tree.column("ID", width=50)
tree.column("Name", width=150)
tree.column("Age", width=50)
tree.column("Gender", width=80)
tree.column("Course", width=120)
tree.pack(fill=BOTH, expand=1)
tree.bind("<ButtonRelease-1>", on_tree_select)

fetch_students()
root.mainloop()
