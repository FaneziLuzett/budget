# app/logic.py
from dataclasses import dataclass
from typing import List

@dataclass
class Transaction:
    type: str  # 'income' or 'expense'
    amount: float
    category: str = ''
    description: str = ''

class BudgetTracker:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_income(self, amount: float, description: str = '') -> None:
        self.transactions.append(Transaction("income", amount, '', description))

    def add_expense(self, amount: float, category: str, description: str = '') -> None:
        self.transactions.append(Transaction("expense", amount, category, description))

    def view_balance(self) -> float:
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        return income - expenses

    def get_transactions(self) -> List[Transaction]:
        return self.transactions
