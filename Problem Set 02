#######################
#Exercise 01
#######################

# Paste your code into this box
monthlyInterestRate = annualInterestRate/12
totalPaid = 0
for month in range(1,13,1):
    minimumMonthlyPayment = balance * monthlyPaymentRate
    balance = balance - minimumMonthlyPayment
    balance =  balance + (balance * monthlyInterestRate)
    totalPaid = totalPaid + minimumMonthlyPayment
    print "Month: " , month
    print "Minimum monthly payment: ", round(minimumMonthlyPayment,2)
    print "Remaining balance: ", round(balance,2)
print "Total paid: ", round(totalPaid,2)
print "Remaining balance: ", round(balance,2)

#######################
#Exercise 02
#######################

# Paste your code into this box
monthlyInterestRate = annualInterestRate/12

initBalance = balance
monthlyPayment = 10
while balance > 0:
    for month in range(1,13,1):
        balance = balance - monthlyPayment
        balance =  balance + (balance * monthlyInterestRate)
    if balance <=0:
        break
    balance = initBalance
    monthlyPayment = monthlyPayment + 10
print "Lowest Payment: ", monthlyPayment

#######################
#Exercise 03
#######################

# Paste your code into this box

monthlyInterestRate = annualInterestRate/12


initBalance = balance
monthlyPaymentLower = initBalance/12.0
monthlyPaymentUpper = (initBalance * (1 + monthlyInterestRate)**12)/12.0
N=0
while N <= 10000:
    monthlyPayment = (monthlyPaymentLower+monthlyPaymentUpper)/2 # new midpoint
    for month in range(1,13,1):
        balance -= monthlyPayment
        balance += balance * monthlyInterestRate
    if balance == 0: # or (monthlyPaymentUpper-monthlyPaymentLower)/2 < 0.01:
        break
    elif balance < 0:
        N += 1
        monthlyPaymentUpper = monthlyPayment
        balance = initBalance
    else:
        N += 1
        monthlyPaymentLower = monthlyPayment
        balance = initBalance

print "Lowest Payment: ", round(monthlyPayment,2)
