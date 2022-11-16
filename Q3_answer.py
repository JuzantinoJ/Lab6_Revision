def readInitialInventoryFromFile():
    key_list = []
    value_list = []
    # inventory = {'a1':['pen', 5], 'a2':['mouse',5] … }
    f = open('inventory.dat', 'r')
    for line in f.readlines():
        key_name, v1, v2 = line.strip().split(' ')
        key_list.append(key_name)
        value_list.append([v1,int(v2)])
        # print("$$$$$key_list:", key_list)
        # print("@@@@value_list:", value_list)
    
    # print("zip(key_list,value_list):", zip(key_list,value_list))

    result = dict(zip(key_list,value_list))
    # print(result)
    
    return result
#print(readInitialInventoryFromFile())

def getOption():
    return int(input('''Menu
1. Add new inventory
2. Ship inventory
3. Print inventory
4. Update file inventory
0. Quit
Enter option: '''))

def addProductCode(curInv):
    
    while True:
        id = input("Enter inventory id: ")
        if id in curInv.keys():
            print("inventory id exists, please enter again.")
        else:
            break
    name = input("Enter inventory name: ")
    qty = input("Enter inventory qty: ")
    curInv[id] = [name, int(qty)]
    print("####curInv",curInv)
    print('The new inventory has been added successfully')
    return curInv

sample_in = {'a1': ['pen', 5], 'a2': ['mouse', 5], 'a3': ['keyboard', 4], 'a4': ['earphone', 10]}

#print(addProductCode(sample_in))

def ship(curInv):
    
    while True:
        id = input("Enter inventory id: ")
        if id not in curInv.keys():
            print("inventory id does not exist, please enter again.")
        else:
            break
    print("name: ", curInv[id][0])
    print("qty: ", curInv[id][1])
    while True:
        qty = int(input("Enter qty to ship: "))
        if int(curInv[id][1]) - qty < 0:
            print("not enough qty to ship, please enter again.")
        else:
            break   
     
    curInv[id][1] = int(curInv[id][1]) - qty
    
    print("curInv",curInv)
    print('The inventory has been updated successfully')
    return curInv

# ship(sample_in)

def inventorySummary(curInv):
    print(f"{'Id':6} {'Name':<15} {'Qty':<5} {'Remarks':<30} ")
    for k, v in curInv.items():
        
        print(f'{k:6} {v[0]:<15} {v[1]:<5} {"Need to reorder" if int(v[1]) < 5 else "":<30}')

def updateFile(dict):
    outfile = open("inventory.dat","w")
    for k,v in dict.items():
        print("{} {} {} ".format(k,v[0],v[1]), file=outfile)
        
    outfile.close()

def main():
    currentinventory = readInitialInventoryFromFile()
    while True:
        option = getOption()
        if option == 1:
           currentinventory = addProductCode(currentinventory)
        elif option == 2:
            currentinventory = ship(currentinventory)
        elif option == 3:
            inventorySummary(currentinventory)
        elif option == 4:
            updateFile(currentinventory)
        elif option == 0:
            break
        else:
            print('Invalid menu option') 
    print('Application ends')  
main()