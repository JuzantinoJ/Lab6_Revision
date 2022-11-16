# d. The station wants to track the number of litres pumped for each pump. 
# Make use of a list to accumulate the litres input for each pump. 
# When the program ends, display the summary as follows:
# Summary Report
# Pump Type Total Litres
# 1 Super 1200
# 2 Unleaded 97 1059
# ...
# You may introduce other lists such as one to store the petrol types etc.

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

# USES LIST TO INCREMENT VALUES AND GET THE VALUE USING SLICE INDEX
def Q1_c():
    price = [0, 2.50, 2.00, 1.50, 1.20]
    litresPumped = [0,0,0,0,0]
    totalSales = [0,0,0,0,0]
    while True:
        choice = getValidInput()
        if 1 <= choice <= 4:
            lt = float(input("Litres pumped: "))
            #use index to find the price of choice 
            litresPumped[choice] += lt
            totalSales[choice] += price[choice]*lt
            print('Please pay ${:.2f}'.format(price[choice]*lt))
        else:
            print('''
            Summary Report
            Pump  Type         Total Litres
            1     Super        {}
            2     Unleaded 97  {}
            3     Unleaded 95  {}
            4     Diesel       {}

            '''.format(litresPumped[1],litresPumped[2],litresPumped[3],litresPumped[4]))
            print('''
            Total Sales
            Pump  Type         Total Sales
            1     Super        ${}
            2     Unleaded 97  ${}
            3     Unleaded 95  ${}
            4     Diesel       ${}

            '''.format(totalSales[1],totalSales[2],totalSales[3],totalSales[4]))
            break
Q1_c()