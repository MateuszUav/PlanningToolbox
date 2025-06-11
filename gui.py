import tkinter as tk
from tkinter import messagebox
import hashlib
import datetime
from db_inserter import FitnessDBInserter

DB_USER = "s30765"
DB_PASSWORD = "oracle12"
DB_DSN = "db-oracle.pjwstk.edu.pl:1521/baza.pjwstk.edu.pl"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def show_register_window():
    def register_user():
        try:
            username = username_entry.get()
            email = email_entry.get()
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            birth_date = datetime.datetime.strptime(birth_entry.get(), "%Y-%m-%d").date()
            password = password_entry.get()

            if not all([username, email, password]):
                raise ValueError("Fields cannot be empty.")

            hashed_pw = hash_password(password)

            db = FitnessDBInserter(DB_USER, DB_PASSWORD, DB_DSN)
            user_id = db.insert_user(username, email, weight, height, birth_date)
            db.insert_password(user_id, hashed_pw)
            db.commit()
            db.close()

            messagebox.showinfo("Success", f"User '{username}' registered (ID: {user_id})")
            register_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root.withdraw()
    register_window = tk.Toplevel(root)
    register_window.grab_set()  # This makes it modal

    register_window.title("Register")

    tk.Label(register_window, text="Username").grid(row=0, column=0)
    username_entry = tk.Entry(register_window)
    username_entry.grid(row=0, column=1)

    tk.Label(register_window, text="Email").grid(row=1, column=0)
    email_entry = tk.Entry(register_window)
    email_entry.grid(row=1, column=1)

    tk.Label(register_window, text="Weight (kg)").grid(row=2, column=0)
    weight_entry = tk.Entry(register_window)
    weight_entry.grid(row=2, column=1)

    tk.Label(register_window, text="Height (cm)").grid(row=3, column=0)
    height_entry = tk.Entry(register_window)
    height_entry.grid(row=3, column=1)

    tk.Label(register_window, text="Birth Date (YYYY-MM-DD)").grid(row=4, column=0)
    birth_entry = tk.Entry(register_window)
    birth_entry.grid(row=4, column=1)

    tk.Label(register_window, text="Password").grid(row=5, column=0)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=5, column=1)

    submit_button = tk.Button(register_window, text="Register", command=register_user)
    submit_button.grid(row=6, column=0, columnspan=2)

def show_login_window():
    def login_user():
        try:
            username = username_entry.get()
            password = password_entry.get()
            hashed_pw = hash_password(password)

            db = FitnessDBInserter(DB_USER, DB_PASSWORD, DB_DSN)
            db.cursor.execute("""
                SELECT ua.user_id
                FROM user_account ua
                JOIN user_password up ON ua.user_id = up.user_id
                WHERE ua.username = :username AND up.password_hash = :pw AND up.active = 'Y'
            """, {"username": username, "pw": hashed_pw})

            result = db.cursor.fetchone()
            db.close()

            if result:
                messagebox.showinfo("Success", f"Welcome, {username} (user_id={result[0]})")
                login_window.destroy()
            else:
                messagebox.showerror("Failed", "Invalid username or password.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root.withdraw()
    login_window = tk.Toplevel(root)
    login_window.grab_set()
    login_window.title("Login")

    tk.Label(login_window, text="Username").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Password").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    submit_button = tk.Button(login_window, text="Login", command=login_user)
    submit_button.grid(row=2, column=0, columnspan=2)

# Main launcher
root = tk.Tk()
root.title("Welcome")

tk.Button(root, text="Register", command=show_register_window, width=20).pack(pady=10)
tk.Button(root, text="Login", command=show_login_window, width=20).pack(pady=10)

root.mainloop()
