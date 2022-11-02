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
        author = input("enter the book author:")
        title = input("enter the title of the book")
        category = input("enter the category of the book")
        charge = input("enter the charge of the book")
        sql = 'INSERT INTO `book`(`author`, `title`, `category`, `charge/day`) VALUES(%s,%s,%s,%s)'
        data =(author,title,category,charge)
        mycursor.executed(sql,data)
        mydb.commit()

    elif(choice==2):
        print('view all book selected')  
        sql = 'SELECT `bookid`, `author`, `title`, `category`, `charge/day` FROM `book`' 
        mycursor.executed(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print("search a book selected") 
        title = input('enter a book title:')
        sql = "SELECT * FROM `book` WHERE `title`='"+title+"'"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print("update the book selected")
        title = input("enter a book name:")
        author = input("enter author name to be updated:")
        category = input("enter category to be updated:")
        charge = input("enter the charge to be updated")
        sql = "UPDATE `book` SET `author`='"+author+"',`title`='"+title+"',`category`='"+category+"',`charge/day`='"+charge/day+"' WHERE `title`='"+title+""
        mycursor.execute(sql)
        mydb.commit()
        print("data updated sucessfully")

    elif(choice==5):
         print("delete the book") 
    elif(choice==6):
        break               