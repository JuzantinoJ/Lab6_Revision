# 1. The pump prices at a petrol station are as follows:
# Pump      Type          Price/litre
# 1         Super           $2.50
# 2         Unleaded 97     $2.00
# 3         Unleaded 95     $1.50
# 4         Diesel          $1.20
#    
# a. Write a program to prompt for a pump number, the litres pumped, 
# and displays the price. The program allows for multiple inputs, 
# until user enters 0 when prompted for the pump number. 
# The program should validate pump number and must keep prompting user until 
# he enters 0 to 4 for pump number. E.g.
#             Enter pump no: 1
#             Litres pumped: 22.5
#             Please pay $56.25
#             Enter pump no: 0
#             (program ends)

# 1a) 
def calculatePrice(no, litres):
    if no == 1:
        #super
        return litres * 2.5 
    elif no == 2:
        #unleaded 97
        return litres * 2
    elif no == 3:
        #unleaded 95
        return litres * 1.5
    elif no == 4:
        #diesel
        return litres * 1.2 

# WHILE LOOP - REPEAT UNTIL ENTER 0
def petrolStation():
    while True:
        pumpNo = int(input("Enter pump no: "))
        if pumpNo != 0:
            litresPumped = float(input("Litres pumped: "))
            price = calculatePrice(pumpNo, litresPumped)
            print('Please pump ${:.2f}'.format(price))
        else:
            print('Program ends')
            break


def main():
    petrolStation()    
# main()

#answer
def Q1_a():
    price = (0, 2.50, 2.00, 1.50, 1.20)
    while True:
        choice = int(input('''       Pump Type        Price/litre 
        1 Super              $2.50 
        2 Unleaded 97        $2.00
        3 Unleaded 95        $1.50
        4 Diesel             $1.20
        Enter pump no: '''))
        if choice == 0:
            break
        
        if 1 <= choice <= 4:
            lt = float(input("Litres pumped: "))
            print('Please pay ${:.2f}'.format(price[choice]*lt))
        else:
            print(f'Invalid pump no {choice}')
    print('(program ends)')
Q1_a()
