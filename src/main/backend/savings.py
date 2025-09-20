from savings_input  import SavingsInput
class SavingsTrack:
    def __init__(self):
        self.savingsList=[]

    def addSavings(self,id, acc_holder_name,bank_name,amount,per_return, exp_in_months, country):
        savings = SavingsInput(id,acc_holder_name,bank_name,amount,per_return, exp_in_months,  country)
        self.savingsList.append(savings)

    def listSavings(self):
        SavingsInput.savings_list(self.savingsList)

if __name__ == "__main__":
    savingsTrack = SavingsTrack()
    savingsTrack.addSavings(101, 'Subathra',"lloyds",500.00, 5.5,10,'United Kingdom')
    savingsTrack.addSavings(102, 'Subat23hra',"llo234yds",500.00, 5.5,10, 'United Kingdom')
    savingsTrack.listSavings()