balance = 10000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount! Enter an amount greater than zero.")

    elif amount > balance:
        print("Insufficient balance!")

    else:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)

except ValueError:
    print("Invalid input! Please enter a valid number.")

else:
    print("Transaction process completed.")

finally:
    print("Thank you for using our ATM!")
