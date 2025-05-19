import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from .logic import BudgetTracker

class BudgetTrackerApp:
    def __init__(self, root):
        self.tracker = BudgetTracker()
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("450x400")
        self.root.configure(bg="#f5f5f5")

        title = tk.Label(root, text="\U0001F4B0 Budget Tracker", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
        title.pack(pady=20)

        button_frame = tk.Frame(root, bg="#f5f5f5")
        button_frame.pack(pady=10)

        btn_style = {"width": 20, "height": 2, "fg": "white", "font": ("Helvetica", 10, "bold")}

        tk.Button(button_frame, text="Add Income", command=self.add_income, bg="#4CAF50", **btn_style).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", **btn_style).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="View Balance", command=self.view_balance, bg="#4CAF50", **btn_style).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="View Transactions", command=self.view_transactions, bg="#4CAF50", **btn_style).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Exit", command=root.quit, bg="#f44336", **btn_style).grid(row=4, column=0, padx=5, pady=10)

    def add_income(self):
        amount = simpledialog.askfloat("Add Income", "Enter income amount in Rands:")
        if amount is not None:
            desc = simpledialog.askstring("Add Income", "Enter description (optional):")
            self.tracker.add_income(amount, desc or "")
            messagebox.showinfo("Success", "Income added successfully! ✅")

    def add_expense(self):
        amount = simpledialog.askfloat("Add Expense", "Enter expense amount in Rands:")
        if amount is not None:
            category = simpledialog.askstring("Add Expense", "Enter category:")
            desc = simpledialog.askstring("Add Expense", "Enter description (optional):")
            self.tracker.add_expense(amount, category or "Uncategorized", desc or "")
            messagebox.showinfo("Success", "Expense added successfully! ✅")

    def view_balance(self):
        balance = self.tracker.view_balance()
        messagebox.showinfo("Current Balance", f"\U0001F4B0 Your Balance is: R{balance:,.2f}")

    def view_transactions(self):
        transactions = self.tracker.get_transactions()
        if not transactions:
            messagebox.showinfo("Transactions", "No transactions recorded yet.")
            return

        top = tk.Toplevel(self.root)
        top.title("Transaction History")
        top.geometry("500x300")

        text_area = tk.Text(top, wrap=tk.WORD, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(top, orient="vertical", command=text_area.yview)
        text_area.configure(yscrollcommand=scrollbar.set)

        for t in transactions:
            tx = f"{t.type.capitalize()}: R{t.amount:,.2f} | "
            if t.type == "expense":
                tx += f"Category: {t.category} | "
            tx += f"{t.description}\n"
            text_area.insert(tk.END, tx)

        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
