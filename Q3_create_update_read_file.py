# (Dictionary)Writeaprogramthehelpsawarehousemanageitsinventory.
# a. The program starts by reading an initial inventory list from a file
# inventory.dat. The content of inventory.dat is as follows:
#          a1 pen 5
#          a2 mouse 5
#          a3 keyboard 4
#          a4 earphone 10
# Write a function readInitialInventoryFromFile() to read the values from the 
# file and store the data in a dictionary in the following format:
# inventory = {'a1':['pen', 5], 'a2':['mouse',5] ... }

#3a

def readInitialInventoryFromFile():
    #readfile
    infile = open('inventory.dat',  'r')
    #create dictionary for inventory
    inventory = {}
    #read file and append into inventory dict
    for file in infile:
        id, product, quantity = file.split()
        inventory[id] =[product, int(quantity)]
    
    infile.close()
    return inventory

    
readInitialInventoryFromFile()

#3b
def addToInventory(dict):
    id = input('id: ')
    product = input('Product: ')
    quantity = int(input('Quantity: '))
    outfile = open('inventory.dat', 'a')
    dict = readInitialInventoryFromFile()
    if id not in dict.keys():
        print(f'{id} {product} {quantity}', file = outfile )
        print("Item added to inventory")
    else:
        print('Id already in file')

    outfile.close

def printInventory(dict):
    print(f"{'Id':6} {'Name':<15} {'Qty':<5} {'Remarks':<30} ")
    for k, v in dict.items():
        print(f'{k:6} {v[0]:<15} {v[1]:<5} {"Need to reorder" if int(v[1]) < 5 else "":<30}')


def shipInventory(dict):
    while True:
        id = input('Select item id to ship: ')
        if id not in dict.keys():
            print('Item not found, please re-enter')
        else:
            break
        
    while True:
        quantity = int(input('Select quantity to ship: '))
        #select itemfrom dictionary [1] is the item index in the list of key value
        if int(dict[id][1] - quantity < 0):
            print('Not enough quantity to ship.')
        else:
            break
    # subtract quantity to ship to the quantity of item
    dict[id][1] = int(dict[id][1]) - quantity
    print("Inventory has been updated. ")
    return dict 

def updateFile(dict):
    outfile = open("inventory.dat","w")
    for k,v in dict.items():
        print("{} {} {} ".format(k,v[0],v[1]), file=outfile)
    print("Inventory Updated")
    outfile.close()

def menu():
    option = int(input('''
    Menu
    1. Add new inventory
    2. Ship inventory
    3. Print inventory
    4. Update inventory file
    0. Quit
    Enter option: 
    '''))
    return option

def main():
    updatedInventory = readInitialInventoryFromFile()
    while True:
        choice = menu()
        if choice == 0:
            break
        elif choice == 1:
            print('Add Items to Inventory')
            #this will auto update inventory 
            updatedInventory = addToInventory(updatedInventory)
        elif choice == 2:
            updatedInventory = shipInventory(updatedInventory)
        elif choice == 3:
            printInventory(updatedInventory)
        elif choice == 4:
            updateFile(updatedInventory)
        else:
            print('Invalid menu option.')
    
main()

#thank you