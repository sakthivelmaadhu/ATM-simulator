# Declare constants.
ACCOUNTNAME = 'name'
PINNUMBER = 'pin'

class Accounts:
    """Class to maintain the account list."""

    # Static variables.
    filename = "./data/accounts.csv"
    members = {}

    def __init__(self):
        self.accountid = ""
        # initialize account details, for the first object creation time only.
        if len(Accounts.members) == 0:
            self.loadAccounts()

    def loadAccounts(self):
        print
        print "Loading account details in members dictionary..."
        Accounts.members.clear()            # Clear if already data is present.

        # Open the file.
        with open(Accounts.filename, "r") as f:
            # Read and load the dictionary
            lines = f.readlines()

        for line in lines:
            if len(line.strip()) > 0:       # process only valid rows, ignore empty lines.
                fields = line.split(",")
                accountid = fields[0].strip()
                accountname = fields[1].strip()
                pinnumber = fields[2].strip()

                Accounts.members[accountid] = {ACCOUNTNAME: accountname, PINNUMBER: pinnumber}


        print Accounts.members

    def validateAccountid(self, accountid):
        # Validate if this is available in dictionary.
        if Accounts.members.has_key(accountid):
            self.accountid = accountid
            return Accounts.members[accountid][ACCOUNTNAME]
        else:
            raise Exception("Invalid account number.")

    def validatePinNumber(self, pinnumber):
        # Validate if this is available in dictionary.
        if Accounts.members.has_key(self.accountid):
            pin = Accounts.members[self.accountid][PINNUMBER]
            return (pin == pinnumber)
        else:
            raise Exception("Invalid account number.")