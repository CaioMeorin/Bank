import json
import os

from ..account.account import Account


class AccountManager:

    def __init__(self, account: Account):
        self._account = account
        self.session_balance = []
        self.op_name: str
        self.withdraw_count = 0
        with open(
            os.path.join(os.path.dirname(__file__), "../operations/operations.json"),
            "r",
        ) as fp:
            self.op = json.load(fp)

    def operations(self, op_name: str, value: float) -> str:
        if op_name == "balance":
            return self.balance_string()

        if op_name == "withdraw":
            if self.account.balance - abs(value) < 0:
                return f"Operation not valid. You can't withdraw {value} from {self.account.balance}"
            elif self.withdraw_count > 2:
                return "Not possible, operation limit reached."

        self.op_name = op_name
        current_op = self.op[op_name]
        try:
            return self.alt_op_logic(current_op, current_op["alternative_cond"], value)

        except KeyError as e:
            return current_op["result"]

    @property
    def account(self):
        """The account property."""
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    def alt_op_logic(self, current_op: str, alternative_cond: str, value: float) -> str:
        if value == 0:
            return current_op["value 0"]
        elif eval(f"{value}{alternative_cond}"):
            return current_op["alternative"].replace("{value}", "%.2f" % value)
        else:
            self.account.balance += value
            self.session_balance.append(
                f"Operation: {self.op_name}; " + f"Value: {value:.2f}"
            )
            if ">" in alternative_cond:
                self.withdraw_count += 1

        return current_op["result"].replace("{value}", f"{value:.2f}")

    def balance_string(self):
        balance_str = (
            "\n----------- BALANCE -----------\n\n"
            + "\n".join(self.session_balance)
            + "\n\n"
            + f"Total: {self.account.balance}"
        )
        return balance_str
