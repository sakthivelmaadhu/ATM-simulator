from atm import accounts
from atm import transactions

class ATMMenu:
    """Integration of accounts and transactions."""

    def __init__(self):
        self.acts = accounts.Accounts()
        self.txn = transactions.Transactions()


    def start(self):
        while True:             # Repeatedly show the menu.
            print( "Tamilnadu Bank Ltd.")
            print
            ano = raw_input("Enter account number: ")

            # Verify the account number.
            try:
                accountname = self.acts.validateAccountid(ano)
                print "Welcome %s" % accountname

            except Exception as e:
                print "Invalid account number. Press Enter to continue..."
                x = raw_input()
                continue

            # Verify pin number.
            pin = raw_input("Enter pin number: ")
            if self.acts.validatePinNumber(pin) == False:
                print "Invalid pin number. Press Enter to continue."
                x = raw_input()
                continue

            self.transactionsMenu()


    def transactionsMenu(self):
        while True:             # Repeatedly show the menu.
            print ("Your option")
            print
            print ("1. Deposit money")
            print ("2. Withdraw money")
            print ("3. List Transactions")
            print ("4. Exit")
            print
            opt = input("Enter option (1-4): ")

            if opt == 4:        # Exit loop
                break
            elif opt == 1:
                amount = input("Enter deposit amount: ")
                self.txn.deposit(self.acts.accountid, amount)
                print ("Deposit successful. Press Enter to continue.")
                raw_input()
                continue

            elif opt == 2:
                amount = input("Enter withdrawal amount: ")
                self.txn.withdraw(self.acts.accountid, amount)
                print ("Withdrawal successful. Press Enter to continue.")
                raw_input()
                continue

            elif opt == 3:
                self.txn.listTransactions(self.acts.accountid)

            else:
                print ("Invalid option. Try again. Press Enter to continue.")
                raw_input()
