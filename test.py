from model import Grocery
import database as db
print('-'*8,'Welcome To Grocery Management System','-'*8)
choice = 0
while (choice!=5):
    print('1-Add new Grocery')
    print('2-Show Grocery List')
    print('3-Delete Grocery')
    print('4-Update Grocery')
    print('5-Exit')
    choice = int(input('Enter your choice '))

    if choice == 1:
        name = input('Enter Grocery Name ')
        price = float(input('Enter Grocery Price '))

        groc = Grocery(name = name,price=price)
        db.saveGroc(groc)
        print('Grocery Saved in Databasee',end='\n\n\n')

    elif choice == 2:
        groclist = db.getGroclist()
        print(7*'-','Grocery list',7*'-')
        for groc in groclist:
            print(groc)
            print('-'*15)
        else:
            print('-'*15)

    elif choice == 3:
        grocId = int(input('Enter GrocId to delete '))
        msg = db.deleteGroc(grocId)
        print('GroceryId',grocId,'is','deleted',end= '\n\n')

    elif choice == 4:
        grocId = int(input('Enter Grocery Id '))
        name = input('Enter Updated Grocery Name ')
        price = float(input('Enter Updated Grocery Price '))
        
        msg = db.updateGroc(name,price)
        print(msg,end='\n\n')

    elif choice == 5:
        print('Good Bye.....')
        db.closeconnection
        print('Database connection is closed successfully...')

    else:
        print('Invalid choice') 


    