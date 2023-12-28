import math

# Ask user if the need a calculator for either investment or bond.
finance_type = input("investment - to calculate the amount of interest you'll earn on your investment"
"\nbond       - to calculate the amount you'll have to pay on a home loan"
"\n "
"\nEnter either 'investment' or 'bond' from the menu above to proceed: ")

finance_type = finance_type.lower() # Convert to lower case to avoid errors from any capitalised letters.

if finance_type == "investment":
    deposit = float(input("Enter how much money would you like to deposit for investment?: "))
    rate = float(input("Enter interest rate (percentage): "))
    years = int(input("Enter how many years you would like to invest for: "))
    interest = input("Simple or Compound interest? ")
    interest = interest.lower()
    
    if interest == "simple":    
# Calculate the amount of simple interest they will receive, based on info inputted.
        interest = deposit * ((1 + (rate / 100) * years))
        print(interest)

    elif interest == "compound":
# Calculate the amount of compond interest they will receive, based on info inputted.
        interest = deposit * math.pow((1 + (rate / 100)), years)
        print(interest)

# Print if words "simple" or "compound" not inputted.
    else:
        print("error: please try again typing in either Simple or Compound")

elif finance_type == "bond":
    current_value = float(input("Enter the current value of the house? "))
    bond_rate = float(input("Enter the interest rate (percentage): "))
    months = int(input("Enter the number of months it will take to repay the bond: "))
    bond_rate = (bond_rate / 100) / 12
# calculate amount user will repay each month using variable inputted above.    
    repayment = (bond_rate * current_value) / (1 - (1 + bond_rate) ** (- months))
    print(repayment)

# Print if words "bond" or "investment" not inputted.
else:
    print("error: please try again typing in either Investment or Bond")
