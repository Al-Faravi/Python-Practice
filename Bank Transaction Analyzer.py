balances = {}

print("Welcome to Simple Bank System")
print("Enter 'done' as name to stop adding users.\n")

while True:
    name = input("Enter your name: ").strip()
    if name.lower() == 'done':
        break

    if name not in balances:
        balances[name] = 0

    while True:
        print(f"\nHello, {name}!")
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("0. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount < 0:
                    print("Cannot deposit a negative amount.")
                    continue
                balances[name] += amount
                print(f"Deposited {amount}. New balance: {balances[name]}")
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount < 0:
                    print("Cannot withdraw a negative amount.")
                    continue
                balances[name] -= amount
                print(f"Withdrew {amount}. New balance: {balances[name]}")
            except ValueError:
                print("Invalid amount.")
        elif choice == '0':
            print(f"Logged out {name}.")
            break
        else:
            print("Invalid choice. Please try again.")

print("\nFinal Account Summary")
for user, balance in balances.items():
    print(f"{user}: {balance}")

if balances:
    richest = max(balances, key=balances.get)
    print(f"\nHighest balance: {richest} with {balances[richest]}")
