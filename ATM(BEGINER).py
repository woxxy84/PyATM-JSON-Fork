import json
import os

DATA_FILE = "atm_data.json"

# Load balance from JSON or set default
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                return data.get("balance", 10000)
        except json.JSONDecodeError:
            return 10000
    return 10000

# Save balance to JSON
def save_data(balance):
    with open(DATA_FILE, "w") as f:
        json.dump({"balance": balance}, f, indent=4)

# Main ATM program
def atm():
    balance = load_data()
    print("💳 Welcome to PyATM! What would you like to do?")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("💰 Your current balance is:", balance)

        elif choice == "2":
            try:
                deposit_value = int(input("💵 Enter amount to deposit: "))
                if deposit_value > 0:
                    balance += deposit_value
                    save_data(balance)
                    print("✅ Deposit successful. New balance:", balance)
                else:
                    print("❌ Invalid amount. Must be positive.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            try:
                withdraw_value = int(input("🏧 Enter amount to withdraw: "))
                if withdraw_value <= balance and withdraw_value > 0:
                    balance -= withdraw_value
                    save_data(balance)
                    print("✅ Withdrawal successful. New balance:", balance)
                else:
                    print("❌ Insufficient funds or invalid amount.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "4":
            print("👋 Goodbye! Thanks for using PyATM.")
            break

        else:
            print("❌ Invalid option. Please choose 1–4.")

# Run the ATM
if __name__ == "__main__":
    atm()
