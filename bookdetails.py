import mysql.connector

mydb=mysql.connector.connect(host = 'localhost', user = 'root' , password = '' ,database= 'librarydb')

mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add book')
    print('2 view all books')
    print('3 search a book')
    print('4 update the book')
    print('5 delete a book')
    print('6 exit')

    choice =int(input('enter an option: '))
    if(choice==1):
        print('book enter selected')
    elif(choice==2):
        print('view all book selected')   
    elif(choice==3):
        print("search a book selected") 
    elif(choice==4):
        print("update the book selected")
    elif(choice==5):
         print("delete the book") 
    elif(choice==6):
        break               