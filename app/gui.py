import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from .logic import BudgetTracker

class BudgetTrackerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Budget Tracker")
        self.root.configure(bg="#f0f0f0")

        self.tracker = BudgetTracker()

        self.btn_style = {
            "font": ("Helvetica", 12),
            "fg": "white",
            "width": 20,
            "height": 2
        }

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="Simple Budget Tracker", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        self._create_buttons(button_frame)

    def _create_buttons(self, frame):
        actions = [
            ("Add Income", self.add_income),
            ("Add Expense", self.add_expense),
            ("View Balance", self.view_balance),
            ("View Transactions", self.view_transactions),
            ("Exit", self.root.quit)
        ]
        for i, (label, command) in enumerate(actions):
            color = "#f44336" if label == "Exit" else "#4CAF50"
            btn = tk.Button(frame, text=label, command=command, bg=color, **self.btn_style)
            btn.grid(row=i, column=0, pady=5)

    def add_income(self):
        try:
            amount = float(simpledialog.askstring("Add Income", "Enter income amount in Rands:"))
            description = simpledialog.askstring("Description", "Enter income description (optional):") or ""
            self.tracker.add_income(amount, description)
            messagebox.showinfo("Success", "Income added successfully.")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    def add_expense(self):
        try:
            amount = float(simpledialog.askstring("Add Expense", "Enter expense amount in Rands:"))
            category = simpledialog.askstring("Category", "Enter expense category:") or "Uncategorized"
            description = simpledialog.askstring("Description", "Enter expense description (optional):") or ""
            self.tracker.add_expense(amount, category, description)
            messagebox.showinfo("Success", "Expense added successfully.")
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    def view_balance(self):
        balance = self.tracker.view_balance()
        messagebox.showinfo("Balance", f"Your current balance is: R{balance:.2f}")

    def view_transactions(self):
        if not self.tracker.has_transactions():
            messagebox.showinfo("Transactions", "No transactions recorded yet.")
            return

        transactions_text = ""
        for idx, t in enumerate(self.tracker.transactions, start=1):
            if t.type == "income":
                transactions_text += f"{idx}. [Income] R{t.amount:.2f} - {t.description}\n"
            else:
                transactions_text += f"{idx}. [Expense] R{t.amount:.2f} - {t.category} - {t.description}\n"

        messagebox.showinfo("Transactions", transactions_text.strip())
