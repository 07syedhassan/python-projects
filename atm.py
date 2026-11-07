balance = 5000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Your Balance:", balance)

elif choice == "2":
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")

elif choice == "3":
    print("Thank you!")

else:
    print("Invalid Choice!")
