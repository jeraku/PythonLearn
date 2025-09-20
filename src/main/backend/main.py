from savings import SavingsTrack

savings = SavingsTrack()

def show_menu():
    print("\n--- Savings Tracking System ---")
    print("1. Add Savings")
    # print("2. Add Member")
    # print("3. Issue Book")
    # print("4. Return Book")
    # print("5. Show Members")
    # print("6. Show Books")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose: ")
        
        if choice == '1':
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            savings.addSavings()
        # elif choice == '2':
        #     n = input("Name: ")
        #     m = input("Member ID: ")
        #     typ = input("Type (student/faculty): ")
        #     library.add_member(n, m, typ)
        # elif choice == '3':
        #     mid = input("Member ID: ")
        #     isbn = input("ISBN: ")
        #     success = library.issue_book(mid, isbn)
        #     print("Issued" if success else "Failed")
        # elif choice == '4':
        #     mid = input("Member ID: ")
        #     isbn = input("ISBN: ")
        #     library.return_book(mid, isbn)
        #     print("Returned")
        # elif choice == '5':
        #     for m in library.members:
        #         m.display_info()
        # elif choice == '6':
        #     for b in library.books:
        #         print(b)
        elif choice == '7':
            print("Good Bye")
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()