class Account:
    def __init__(self, _owner: str, opening_deposit: float):
        self.balance = 0 if opening_deposit <= 0 else opening_deposit
        self._owner = _owner

    @property
    def owner(self):
        """The owner property."""
        return self._owner

    @property
    def balance(self):
        """The balance property."""
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
