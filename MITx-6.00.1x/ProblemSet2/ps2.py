# Problem 1
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
# required by the credit card company each month. The following variables contain values as described below:
#   balance - the outstanding balance on the credit card
#   annualInterestRate - annual interest rate as a decimal
#   monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out
# the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print:
#   Remaining balance: 813.41
# instead of
#   Remaining balance: 813.4141998135

balance = 42 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal
monthlyPaymentRate = 0.04 # minimum monthly payment rate as a decimal

for i in range(13):
    if i == 0:
        #print("Month " + str(i) + " remaining balance : ")
        next
    else:
        abs_payment = balance * monthlyPaymentRate
        balance -= abs_payment
        abs_interest = balance * (annualInterestRate / 12)
        balance += abs_interest
        #print("Month " + str(i) + " remaining balance : " + str(round(balance,2)))

print("Remaining balance: " + str(round(balance,2)))


# Problem 2
# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
# within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
# is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
#   balance - the outstanding balance on the credit card
#   annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for
# example:
#   Lowest Payment: 180
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for
# that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
# possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math
# is found below:
#   Monthly interest rate = (Annual interest rate) / 12.0
#   Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#   Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 3926
annualInterestRate = 0.2

startingPayment = 10
temp_balance = balance

while temp_balance > 0:
    for i in range(1,13):
        temp_balance -= startingPayment
        interest = temp_balance * (annualInterestRate / 12)
        temp_balance += interest

    if temp_balance <= 0:
        break;
    else:
        temp_balance = balance
        startingPayment += 10

print("Lowest Payment: " + str(startingPayment))