# Bank-problem
# Write a Python program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit while W means withdrawal.

  Balance=0
while True:
    n = input("Enter the Operation:\n")
    operation=n.split()   
    value=operation[0]
    amount=int(operation[1])
    if value=="D":
        Balance+=amount
    elif value=="W":
        if amount>Balance:
            print("Insufficient balance")
        else:
            Balance-=amount
    else:
        pass
    choice = input("If you want to exit press y else press n to continue: ")
    if choice== "y" or choice == "Y":
        break
    
    
    print("Total Balance", Balance )
print ("Final Balance", Balance)
