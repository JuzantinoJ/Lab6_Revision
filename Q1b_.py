#Q1b
# Write a function getValidInput() that prompts for a pump no,
# and displays ‘Invalid pump no’ if the pump number is not 0,1,2,3,4. 
# Repeat until pump number is valid. The function returns the valid value. 
# Modify part a, to call this function.


# VALIDATION - REPEAT UNTIL VALID VALUE, USE COMPARISON
def getValidInput():
    while True:
       pumpNo = int(input('''
       Pump  Type         Price/Litre
       1     Super        $2.50
       2     Unleaded 97  $2.00
       3     Unleaded 95  $1.50
       4     Diesel       $1.20
       Enter pump no: '''))
       
       if 0 <= pumpNo <= 4:
            return pumpNo
       else:
            print(f'Invalid pump choice {pumpNo}')

        
def Q1_a():
    while True:
        choice = getValidInput()
        price = (0, 2.50, 2.00, 1.50, 1.20) 
        if 1 <= choice <= 4:
            lt = float(input("Litres pumped: "))
            #use index to find the price of choice 
            print('Please pay ${:.2f}'.format(price[choice]*lt))
        else:
            print('(program ends)')
            break
Q1_a()
