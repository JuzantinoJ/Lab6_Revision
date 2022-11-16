# Create a list for the price/litre data in the table above. 
# Remove the if...elif...else selection in part a. used for 
# computing the price to pay. Modify your code to use the list.

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

        
def Q1_c():
    while True:
        choice = getValidInput()
        price = [0, 2.50, 2.00, 1.50, 1.20]
        if 1 <= choice <= 4:
            lt = float(input("Litres pumped: "))
            #use index to find the price of choice 
            print('Please pay ${:.2f}'.format(price[choice]*lt))
        else:
            print('(program ends)')
            break
Q1_c()
