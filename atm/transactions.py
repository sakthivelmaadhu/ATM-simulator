from datetime import datetime

class Transactions:
    """This class maintains the deposit, withdrawal and listing the transactions."""

    filename = "./data/transactions.csv"

    def deposit(self, accountid, amount):
        # Write the transaction in file.
        with open(Transactions.filename, "a") as f:
            trandate = datetime.now().strftime("%d/%m/%Y %X")
            f.write("{an},{dt},Deposit,{amt}\n".format(an=accountid, dt=trandate, amt=amount))


    def withdraw(self, accountid, amount):
        # Write the transaction in file.
        with open(Transactions.filename, "a") as f:
            trandate = datetime.now().strftime("%d/%m/%Y %X")
            f.write("{an},{dt},Withdraw,{amt}\n".format(an=accountid, dt=trandate, amt=amount))

    def listTransactions(self, accountid):

        # open file.
        with open(Transactions.filename, "r") as f:
            trans = []
            for line in f.readlines():
                fields = line.split(",")
                if fields[0] == accountid:      # filter only for the required accountid
                    trans.append(line.strip())

        # display records.
        print "Transactions"
        print "------------"
        closingBalance = 0
        for trn in trans:
            fields = trn.split(",")
            transdate = fields[1]       # Transaction date.
            trantype  = fields[2]       # Deposit / Withdrawal
            amount = float(fields[3])
            if trantype == "Withdraw":
                amount = -amount

            closingBalance += amount

            print "{} {:<20s} {:10.2f}".format(transdate, trantype, amount)

        print "Closing Balance %.2f" % closingBalance
        print

