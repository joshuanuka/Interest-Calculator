##################################################################
# Student contributions to the interest calculator
#
# You are free to add additional utility functions as you see fit,
# but you must implement each of the following functions while
# adhering to the specifications given in the project description
##################################################################

#---------------------------------------------------------------------------------

def greeting():
    print('This interest calculator will ask you to select an interest rate,')         #The original greeting message
    print('followed by a principal value.  It will then calculate and display')
    print('the principal, interest rate, and balance after one year. You will')
    print('then be invited to execute the process again or terminate.')  



#---------------------------------------------------------------------------------

def getRate(choices):
    print('\nPlease select an interest rate:')
    for k in range(len(choices)):                                                     #counts the number of options
        letters=['A','B','C','D','E','F']
        options=f'{letters[k]}) {choices[k]:2}%'                                      #assigns rates to options
        print(options)
    
    choice=input('Enter'+' '+letters[0]+'-'+letters[len(choices)-1]+':')              #specifies range of options
    choice=choice.strip()
    if choice in letters[:len(choices)]:                                              #checks for correct input
          rate=choices[letters.index(choice)]
          return float(int(rate)/100)
    else:
        print('That is not a valid selection.')
        return getRate(choices)                                                       #runs until correct input
    

#---------------------------------------------------------------------------------

def getPrincipal(limit):
    response=input('\nEnter the principal '+'(limit'+' '+str(limit)+')'+':')
    p=response.replace('$','')
    try:
        float(p)
        if float(p)<0:                                                                  #makes sure input is positive
            print('You must enter a positive amount.\n')
            return getPrincipal(limit)
        if float(p)>limit:                                                              #principal must not be greater than limit
            print('The principal must be at most',str(limit)+'.\n')
            return getPrincipal(limit)
    except ValueError:
        print ('Please enter a number.\n')
        getPrincipal(limit)
    if p.isdigit()==False and '.' not in p:
        print('Please enter a number.\n')
        return getPrincipal(limit)
    
    if '.' in p:
        count=p.split('.')
        if len(count[1])>2:                                                         #ensures there are only two decimal places
            print('The principal must be specified in dollars and cents.\n')
            return getPrincipal(limit)
        else:
            return float(p)
    else:
        return float(p)


#---------------------------------------------------------------------------------

def computeBalance(principal, rate):
    balance= principal+(principal*rate)                                             #amount at the end of the year
    return balance

#---------------------------------------------------------------------------------

def displayTable(principal, rate, balance):                                         #displays the table
    month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    print('Initial Principal   Interest Rate   End of Year Balance')
    print('=======================================================')
    msg=f'${principal:<16.2f}   {rate:<13.2f}   ${balance:<18.2f}'
    print(msg)
    print('\nMonth   Starting Balance    APR     Ending Balance')
             
    print('==================================================')

    
    for m in month:                                                                  #loops through all the months
        annual=rate                                                                  
        monthly = pow(1+annual, 1.0/12) - 1
        endingBalance= principal+(principal*monthly)
        msg2=f'{m:<5}   ${principal:6.2f}  {rate:15.2f}    ${endingBalance:6.2f}'   #alligns figures in the table
        print(msg2)
        principal=endingBalance                                                     #because of continuous compunding of interest
        

#---------------------------------------------------------------------------------


def askYesNo(prompt):                                                               #user prompt to rerun process
    response=input(prompt)
                                                                                    #checks for first letter of response
    if response[0]=='y' or response[0]=='Y':                                         
        return True
    if response[0]=='n' or response[0]=='N':
        return False
    else:
        return askYesNo(prompt)                                                    #makes sure user enters valid input



#---------------------------------------------------------------------------------







