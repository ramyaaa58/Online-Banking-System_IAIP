import tkinter as tk
from tkinter import messagebox

users = {}
current_user = None

def create_account():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Username and Password cannot be empty")
        return

    if username in users:
        messagebox.showerror("Error", "User already exists")
    else:
        users[username] = {
            "password": password,
            "balance": 0,
            "history": ["Account Created"]
        }
        messagebox.showinfo("Success", "Account Created Successfully")


def login():
    global current_user

    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username]["password"] == password:
        current_user = username
        messagebox.showinfo("Success", "Login Successful")
        banking_window()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def banking_window():
    bank = tk.Toplevel(root)
    bank.title("Online Banking System")
    bank.geometry("400x450")

    tk.Label(bank, text="Amount").pack(pady=5)

    amount_entry = tk.Entry(bank)
    amount_entry.pack()

    balance_label = tk.Label(
        bank,
        text=f"Balance : ₹{users[current_user]['balance']}"
    )
    balance_label.pack(pady=10)

    history_box = tk.Text(bank, width=40, height=10)
    history_box.pack()

    def update_history():
        history_box.delete(1.0, tk.END)
        for item in users[current_user]["history"]:
            history_box.insert(tk.END, item + "\n")

    update_history()

    def deposit():
        try:
            amount = float(amount_entry.get())

            if amount <= 0:
                raise ValueError

            users[current_user]["balance"] += amount
            users[current_user]["history"].append(
                f"Deposited ₹{amount}"
            )

            balance_label.config(
                text=f"Balance : ₹{users[current_user]['balance']}"
            )

            update_history()

            messagebox.showinfo("Success", "Amount Deposited")

        except:
            messagebox.showerror("Error", "Enter Valid Amount")

    def withdraw():
        try:
            amount = float(amount_entry.get())

            if amount <= 0:
                raise ValueError

            if amount > users[current_user]["balance"]:
                messagebox.showerror(
                    "Error",
                    "Insufficient Balance"
                )
                return

            users[current_user]["balance"] -= amount

            users[current_user]["history"].append(
                f"Withdrawn ₹{amount}"
            )

            balance_label.config(
                text=f"Balance : ₹{users[current_user]['balance']}"
            )

            update_history()

            messagebox.showinfo("Success", "Amount Withdrawn")

        except:
            messagebox.showerror("Error", "Enter Valid Amount")

    def check_balance():
        messagebox.showinfo(
            "Balance",
            f"Current Balance : ₹{users[current_user]['balance']}"
        )

    tk.Button(bank,
              text="Deposit",
              command=deposit,
              bg="green",
              fg="white").pack(pady=5)

    tk.Button(bank,
              text="Withdraw",
              command=withdraw,
              bg="red",
              fg="white").pack(pady=5)

    tk.Button(bank,
              text="Check Balance",
              command=check_balance).pack(pady=5)

    tk.Button(bank,
              text="Exit",
              command=bank.destroy).pack(pady=5)
    
root = tk.Tk()
root.title("Online Banking System")
root.geometry("350x250")

tk.Label(root, text="ONLINE BANKING SYSTEM",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root,
          text="Create Account",
          command=create_account,
          bg="blue",
          fg="white").pack(pady=5)

tk.Button(root,
          text="Login",
          command=login,
          bg="green",
          fg="white").pack(pady=5)

root.mainloop()