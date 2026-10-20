class BankAccount:
    """Класс для управления банковским счетом."""
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        """Пополняет счет на указанную сумму."""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        self._balance += float(amount)

    def withdraw(self, amount):
        """Снимает указанную сумму со счета."""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")
        self._balance -= float(amount)

    def get_balance(self):
        """Возвращает текущий баланс."""
        return self._balance