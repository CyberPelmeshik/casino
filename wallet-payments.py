"""Модуль кошелька и учета баланса."""

class Wallet:
    """Описывает кошелек игрока.

    Attributes:
        balance: Текущий баланс.
        history: История операций.
    """

    def __init__(self, balance: float = 0) -> None:
        """Создает кошелек с начальным балансом.

        Args:
            balance: Начальный баланс.
        """
        self.balance = balance
        self.history = []

    def deposit(self, amount: float) -> None:
        """Пополняет баланс.

        Args:
            amount: Сумма пополнения.
        """
        self.balance += amount
        self.history.append(f"Deposit: +{amount}")

    def withdraw(self, amount: float) -> None:
        """Списывает средства с баланса.

        Args:
            amount: Сумма списания.
        """
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw: -{amount}")
        else:
            self.history.append("Withdraw failed: insufficient funds")