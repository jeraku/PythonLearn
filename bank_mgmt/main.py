from User import User

users = User()

def show_menu():
    print("\n--- Bank Management System ---")
    print("1. Add a new Account holder info")
    print("2. Add Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show Members")
    print("6. Show Books")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Choice ")
    if choice == '1':
        account_holder_name = input("Enter Account holder name:")
        account_selection = int(input("Please confirm whether its a Savings(1)/Current account(2): "))
        users.add_member(accout_holder_name, account_selection)
    elif choice == '7':
        break
n