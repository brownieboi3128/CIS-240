# Get the loan details
moneyOwed = 50000
apr = 3
payment = 1000
months = 60

# Divide apr by 100 to make a percent, and 12 to make monthly
monthlyRate = apr / 100 / 12
print(f"Month\tMonthly Payment\t\tInterest Paid\t\tLoan Balance")
# Loop through each month
for month in range(months):
    interestPaid = moneyOwed * monthlyRate
    moneyOwed = moneyOwed + interestPaid
    moneyOwed = moneyOwed - payment
    print(f"{month}\t${payment:,.2f}\t\t${interestPaid:,.2f}\t\t\t${moneyOwed:,.2f}")
    if (moneyOwed - payment < 0):
        print(f"The last payment is ${moneyOwed:,.2f}")
        print("You paid off the loan in", month + 1, "months")
        break


#Print results after this month
#print(f"Paid ${payment:,.2f} of which ${interestPaid:,.2f} was interest.", end=" " )
#print(f"Now I owe ${moneyOwed:,.2f}")
