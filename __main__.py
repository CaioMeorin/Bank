import os
import sys

from .src.account.account import Account
from .src.managers.account_manager import AccountManager

WELCOME_MESSAGE = """

Welcome to Very Simple Banking.

(You can re-visit this screen by pressing "h")

d - Deposit;
w - Withdraw;
b - Check balance;

q - Exit.

"""


def main():
    account = Account(input("Client name: "), float(input("Initial deposit: ")))
    am = AccountManager(account)
    print(WELCOME_MESSAGE)
    while True:
        event = input()
        if event == "d":
            print(am.operations("deposit", int(input("Deposit: "))))
        elif event == "w":
            print(am.operations("withdraw", int(input("Withdraw: "))))
        elif event == "b":
            print(am.operations("balance", 0))
        elif event == "q":
            break


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
    sys.exit(0)
