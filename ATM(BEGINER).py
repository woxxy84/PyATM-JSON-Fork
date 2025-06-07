
Balance = 10000
print("Welcome to our ATM, What would you like to do?")

while True:
    print("1. Check the balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Your balance is:", Balance)
        print("Thanks you for using our programme")
    elif choice == "2":
        deposit_value = int(input("How much do you want to deposit?: "))
        balance = Balance + deposit_value
        print("Your updated balance is:", balance)
    elif choice == "3":
        withdraw_value = int(input("How much do you want to withdrawal?: "))
        if withdraw_value <= Balance:
            Balance -= withdraw_value
            print("Your updated balance is:", Balance)
        else:
            print("Insufficient funds")
    elif choice == "4":
        print("Goodbye!")
        break