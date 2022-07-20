###########################################################################
# Main program for interest calculator
#
# Do not change this file. All student work should be in interestStudent.py
###########################################################################
from random import sample, randint
from interestcalculator import *

greeting()
active = True
while active:
    choices = sorted(sample(range(1,20), randint(2,6)))
    rate = getRate(choices)
    principal = getPrincipal(100000 * randint(5,10))
    balance = computeBalance(principal, rate)
    print()
    displayTable(principal, rate, balance)
    print()
    active = askYesNo('Another Computation [y/n]? ')
print('Quitting program. Bye.')
