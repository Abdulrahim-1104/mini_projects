import json
from datetime import datetime
import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",passwd="1104")
mycursor = connection.cursor()
suffix = '_library'
def createLibrary(lib_name):
    mycursor.execute(f"create database {lib_name}")
    mycursor.execute(f"use {lib_name}")
    mycursor.execute("create table users(cardNo varchar(20),username varchar(20),mobile_number varchar(10), booklist json)")
    mycursor.execute("create table library_books (bookname varchar(100))")

def deleteLibrary(lib_name):
    mycursor.execute(f"drop schema {lib_name}")

def addBooksToLibrary(lib_name,books):
    mycursor.execute(f'use {lib_name}')
    query = f"insert into library_books values (%s)"
    for book in books:
        mycursor.execute(query,(book,))
        connection.commit()

def removeBooksToLibrary(lib_name,books):
    mycursor.execute(f'use {lib_name}')
    query = f"delete from library_books where bookname = (%s)"
    for book in books:
        mycursor.execute(query, (book,))
        connection.commit()

def displayLibrary():
    print('-- Libraries --')
    [print(library) for library in libraries()]

def isAlreadyMember(lib_name,username,mobile_number):
    mycursor.execute(f'use {lib_name}')
    query = f'select cardNo from users where username = %s and mobile_number = %s'
    mycursor.execute(query,(username,mobile_number))
    cardNo =  mycursor.fetchone()
    return cardNo

def createId(lib_name,username,mobile_number):
     mycursor.execute(f'use {lib_name}')
     mycursor.execute('select count(username) from users')
     card_prefix = lib_name[0:4]
     card_suffix = mycursor.fetchall()
     card_no = card_prefix + str(card_suffix[0][0]+1)
     book_list = json.dumps([])
     query = 'insert into users values (%s,%s,%s,%s)'
     mycursor.execute(query,(card_no,username,mobile_number,book_list))
     connection.commit()
     return card_no

def isValidCard(card_number):
    databases = libraries()
    for db in databases:
        mycursor.execute(f'use {db}')
        mycursor.execute('select cardNo from users')
        db_users = [user[0] for user in mycursor.fetchall()]
        if card_number in db_users:
            return db
    return None

def user_books(lib_name,card_number):
    mycursor.execute(f'use {lib_name}')
    query = 'select booklist from users where cardNo = %s'
    mycursor.execute(query,(card_number,))
    books =  mycursor.fetchall()[0][0]
    return json.loads(books)

def isBookInUserBooklist(lib_name,card_number,bookname):
    userBooks = user_books(lib_name,card_number)
    for book in bookname:
        if book in userBooks:
            return True
    return False

def submitBooks(lib_name,card_number,bookname):
    addBooksToLibrary(lib_name,bookname)
    bookRemoved = list(filter(lambda book: book != bookname, user_books(lib_name, card_number)))
    booksInJson = json.dumps(bookRemoved)
    mycursor.execute(f'use {lib_name}')
    query = "UPDATE users SET booklist = %s WHERE cardNo = %s"
    mycursor.execute(query,(booksInJson,card_number))
    connection.commit()

def displayAvailableBooks(lib_name):
    mycursor.execute(f'use {lib_name}')
    mycursor.execute("select * from library_books")
    books = mycursor.fetchall()
    [print(book[0]) for book in books]
    if len(books):
        return True
    return False

def isBookInLibrary(lib_name, bookname):
    mycursor.execute(f'use {lib_name}')
    mycursor.execute('select * from library_books')
    return mycursor.fetchall()
def purchaseBook(lib_name,card_number,book):
    removeBooksToLibrary(lib_name,book)
    book_list = user_books(lib_name, card_number)
    [book_list.append(b) for b in book]
    json_format = json.dumps(book_list)
    mycursor.execute(f'use {lib_name}')
    query = "UPDATE users SET booklist = %s WHERE cardNo = %s"
    mycursor.execute(query,(json_format,card_number))
    connection.commit()

def start():
    while True:
        print('1. Admin')
        print('2. User')
        print('3. Exit')
        o1 = int(input('Enter the options : '))
        if o1 == 1:
            print('1. Create Library....')
            print('2. Delete Library....')
            print('3. Add books to you library')
            print('4. Remove books from your library')
            print('5. Back')
            o2 = int(input('Enter the options : '))
            if o2 == 1:
                while True:
                    lib_name = input('Enter the library name : ')+suffix
                    if libraries() is not None and lib_name in libraries():
                        print('The library name is already exist')
                        print('Try a different name')
                    else:
                        createLibrary(lib_name)
                        print('Library created successfully')
                        break
            elif o2 == 2:
                while True:
                    lib_name = input('Enter the library name to delete : ')+suffix
                    if lib_name in libraries():
                        deleteLibrary(lib_name)
                        print('Your library has deleted successfully....')
                        break
                    else:
                        print('The name of the library is not exists ')
            elif o2 == 3:
                while True:
                    lib_name = input('Enter you library name : ')+suffix
                    if lib_name not in libraries():
                        print('The library you entered is not exists')
                    else:
                        books = input('Enter your book names to store in library\nNote:books name must seprated by comma(,) : ').split(',')
                        addBooksToLibrary(lib_name, books)
                        print('Books added to '+ lib_name +' Library')
                        print('Here you book list')
                        displayAvailableBooks(lib_name)
                        break
            elif o2 == 4:
                while True:
                    lib_name = input('Enter you library name : ')+suffix
                    if lib_name not in libraries():
                        print('The library you entered is not exists')
                    else:
                        books = input('Enter your book names to remove in library\nNote:books name must seprated by comma(,) : ').split(',')
                        removeBooksToLibrary(lib_name, books)
                        print('Books removed to '+ lib_name +' Library')
                        break
            elif o2 == 5:
                break
            else:
                print('Invalid option')
        elif o1 == 2:
            while True:
                print('select options')
                print('1. Register')
                print('2. Already a member')
                print('3. Exit')
                opt1 = int(input('Enter your options : '))
                if opt1 == 1:
                    print('Registration Process')
                    displayLibrary()
                    lib_name = input('Enter the library you have to register : ')+suffix
                    if lib_name in libraries():
                        name = input('Enter your name :')
                        mobile_number = input('Enter your mobile number : ')
                        if isAlreadyMember(lib_name,name, mobile_number):
                            print('You are already our member try to login')
                        else:
                            card_number = createId(lib_name,name, mobile_number) #this will return card no genered by this method
                            print(f'Your card number is {card_number}')
                            print('Kindly dont share with any one')
                            print('Please Login')
                    else:
                        print('The library you entered is not exits')
                        print('Please check the available libraries')
                elif opt1 == 2:
                    while True:
                        print('1. Enter via card ')
                        print('2. Forgot card number ')
                        print('3. Exit')
                        opt2 = int(input('Enter you options : '))
                        if opt2 == 1:
                            card_number = input('Enter you card number : ')
                            lib_name = isValidCard(card_number)
                            if lib_name:
                                user_book_list = user_books(lib_name,card_number)
                                if len(user_book_list) == 0:
                                    print('You didnt purchased any book yet')
                                else:
                                    print('Your already purchased books')
                                    for books in user_book_list: print(books)
                                while True:
                                    print('1. Submit books')
                                    print('2. Purchase books')
                                    print('3. Exit')
                                    opt3 = int(input('Enter you options : '))
                                    if opt3 == 1:
                                        book_name = input('Enter the book name your going to submit : ').split(',')
                                        if isBookInUserBooklist(lib_name,card_number,book_name):
                                            submitBooks(lib_name,card_number,book_name)
                                            print('Book submitted successfully....!')
                                        else:
                                            print('You didnt purchased the book yet')
                                    elif opt3 == 2:
                                        available_books = displayAvailableBooks(lib_name)
                                        if not available_books:
                                            print('Library have no books all book have purchased come after some days')
                                            continue
                                        book_name = input('Enter the book you want to purchase : ').split(',')
                                        if isBookInLibrary(lib_name,book_name):
                                            purchaseBook(lib_name,card_number,book_name)
                                            print('You successfully purchased the book')
                                            continue
                                        print('There is no book in library named' + book_name)
                                        print('Please check menu to purchase the available books')
                                    elif opt3 == 3:
                                        break
                                    else:
                                        print('Invalid option enter the valid one')
                            else:
                                print('Invalid card number')
                                print('Please check your given card number is valid')
                        elif opt2 == 2:
                            lib_name = input('Which library member are you ? : ')+suffix
                            name = input('Enter you name : ')
                            mobile_number = input('Enter you mobile number : ')
                            card_number = isAlreadyMember(lib_name,name, mobile_number)
                            if card_number:
                                print(f'Here is you card number have a good day {card_number}')
                            else:
                                print('You are not a member yet')
                                print('Try to register to be a memeber')
                        elif opt2 == 3:
                            break
                        else:
                            print('Invalid Option ')
                elif opt1 == 3:
                    break
                else:
                    print('Invalid option enter the valid one')
        elif o1 == 3:
            print('Thank you Visit Again')
            break
        else:
            print('Invalid option')

def libraries():
    pattern = '%library'
    mycursor.execute('SHOW DATABASES LIKE %s', (pattern,))
    return [item[0] for item in mycursor.fetchall()]
if __name__ == "__main__":
    start()
