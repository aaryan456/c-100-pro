class ATM(object):
    
    def __init__(self,company,limit):
        self.company = company
        self.limit = limit
    
    def amount(self):
        print("Max Amount that can be transacted = 2000")

    def Debited(self):
        print("Given")
    
bank = ATM("limit",8000)

print(bank.amount())
print(bank.Debited())
