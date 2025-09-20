from datetime import date
from dateutil.relativedelta import relativedelta

class SavingsInput:
    def __init__(self,id, acc_holder_name,bank_name,amount,per_return, exp_in_months, country):
        self.id = id
        self.acc_holder_name = acc_holder_name
        self.bank_name= bank_name
        self.amount = amount
        self.percentage_return = per_return
        self.exp_date = date.today() + relativedelta(months=+exp_in_months)
        self.created_date = date.today()
        self.status = "active"
        self.country = country

    def savings_list(savingsList):
        for list_savings in savingsList:
            print(" | ".join(f"{attr}: {value}" for attr, value in list_savings.__dict__.items()))

if __name__ == "__main__":
    savingsTrack = SavingsInput (101, 'Subathra',"lloyds",500.00, 5.5,4,'United Kingdom')
    savings_List_track = []
    savings_List_track.append(savingsTrack)
    SavingsInput.savings_list(savings_List_track)
    print(savingsTrack)
