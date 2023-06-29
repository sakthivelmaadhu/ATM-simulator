from atm import accounts
from atm import transactions

acts = accounts.Accounts()

# acts.loadAccounts()

try:
    accountname = acts.validateAccountid('1')
    print ("Valid account id: " + accountname)

    if acts.validatePinNumber("1111"):
        print ("Valid pin number entered.")

        # Testing deposit.
        txn = transactions.Transactions()
        # txn.withdraw(acts.accountid, 450)
        txn.listTransactions(acts.accountid)
        del txn
    else:
        print ("Invalid pin number.")
except Exception as e:
    print ("Error: " + e.message)

del acts
