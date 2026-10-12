# Assignment 1 – Bank ATM Console Application
# Build a Bank ATM Console Application in Python using operators, conditions, and loops
# only.
# Requirements:
# ● Display an ATM menu with options: Check Balance,Deposit Money,Withdraw
# Money ,Exit
# ● Start with a default account balance.
# ● Allow the user to check their current balance.
# ● Allow the user to deposit money and update the balance.
# ● Allow the user to withdraw money only when sufficient balance is available.
# ● Display an appropriate message for insufficient balance.
# ● Use conditional statements to handle different ATM operations.
# ● Use a loop to keep displaying the ATM menu until the user chooses to exit.
# ● Use arithmetic and comparison operators for balance calculations and
# validations.
# ● Display appropriate messages after each transaction.
i = 0
balance = 10000
while i<=4:
    print("1:Check Balance")
    print("2:Deposit money")
    print("3:Withdraw money")
    print("4:Exit")
    i = int(input("Enter a number from 1 to 4:"))
    if i == 1:
        print("Balance: ",balance)
    elif i == 2:
        deposit = int(input("Enter the amount:"))
        balance = deposit+balance
        print("Amount deposited=",deposit)
        print("Your updated balance is: ",balance)
    elif i==3:
        withdraw = int(input("Enter amount to withdraw:"))
        if withdraw<=balance:
            print("Withdraw successful")
            balance = balance-withdraw
            print("Your updated balance is: ",balance)
        else:
            print("Insufficent balance")
    elif i==4:
        print("EXIT")
        break
else:
    print("Enter a correct option")    
