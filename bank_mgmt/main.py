from BankAccount import BankAccount

bank_account = BankAccount()

def show_menu():
    print("\n--- Bank Management System ---")
    print("1. Add a new Account holder info")
    print("2. List Member")
    print("3. Deposit amount")
    # print("4. Return Book")
    # print("5. Show Members")
    # print("6. Show Books")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Choice ")
    if choice == '1':
        account_holder_name = input("Enter Account holder name:")
        # account_holder_age = input("Enter your age:")
        account_holder_age = 50
        account_holder_password = "123456"
        # account_selection = int(input("Please confirm whether its a Savings(1)/Current account(2): "))
        account_selection = 1
        # account_holder_isemployee = input("Please confirm your whether you are an employee Yes/No: "  )
        account_holder_isemployee = False
        bank_account.add_member(account_holder_name, account_holder_age,account_holder_password,account_selection, account_holder_isemployee)
    elif choice== "2":
        bank_account.list_member()
    elif choice== "3":
        account_info = input("Enter your username/account id:")
        deposit_amount=500
        # if(account_info.isdigit()):
        #     account_info=100
        # else:
        acc_info=account_info
        bank_account.deposit_money(acc_info, deposit_amount)


    elif choice == '7':
        break
