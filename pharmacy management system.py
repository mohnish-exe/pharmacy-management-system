

import mysql.connector
from tabulate import tabulate                 
from datetime import date
from tkinter import *
import time
from tkinter import messagebox


con=mysql.connector.connect(host="localhost",user="root",password="root")
cur=con.cursor()


cur.execute("use pysales_inventory")
cur.execute("create table if not exists stock(product_code varchar(25) primary key,product_name varchar(25) not null,quantity varchar(25) not null,price varchar(25) not null)")
cur.execute("create table if not exists purchase (purchased_date DATE NOT NULL, phone_no VARCHAR(25) NOT NULL, pcode VARCHAR(25) NOT NULL, total_purchased_amount DECIMAL(10, 2) NOT NULL)")
cur.execute("create table if not exists login(username varchar(25) not null,password varchar(25) not null)")
cur.execute("create table if not exists cart(PRODUCT_CODE varchar(25) not null, PRODUCT_NAME varchar(50) not null, QUANTITY_CHOSEN varchar(25) not null,PRICE decimal(10,2) not null)")
cur.execute("create table if not exists bill(description varchar(50) not null, quantity varchar(50) not null ,total decimal(10,2) not null,unit_price decimal(10,2))")


cur.execute("select * from login")#==>Empty table

j=0
for i in cur:
    admin,paswrd=i
    j=1
if(j==0):
    cur.execute("insert into login values('admin','1234')") # Default password
if(j==1):
    pass

con.commit()

def value_exists(value):
     # Execute a query to check if the value exists in the table
     cur.execute("SELECT COUNT(*) FROM stock WHERE pcode={}".format(value))
     count = cur.fetchone()[0]
     return count > 0

def check_value_exists(value):
    # Execute a query to check if the value exists in the table
    cur.execute('select pcode from stock')
    fetch = cur.fetchall()
    pcodlist = [h[0] for h in fetch]
    if value in pcodlist:
        return 1
    else:
        return 0

def get_valid_value():
    while True:
        product_code1 = input()
        if not product_code1.isdigit():
            print("Enter numeric values only.")
            continue
        elif check_value_exists(int(product_code1)):
            return int(product_code1)
        else:
            print("Value not found. Please enter a valid value.")


def passsword():
        global c
        c=0
        def submit():

            password=pw.get()
            if paswrd==password:
                global c
                c+=1
                messagebox.showinfo("Success!!","Logged in successfully")
                top.destroy()
            else:
                messagebox.showinfo("Access Denied!!","Entered password is incorrect, Please Try              Again!")
        top = Tk()
        top.geometry("450x300")
        Label(top,text = "Admin Screen",font=('Calibri',20)).place(x = 130,y = 60) # the label for user
        Label(top,text = "Password").place(x = 40, y = 100)
        Button(top,text = "Submit",command=submit).place(x = 180, y = 130)
        def submitf(event):
            submit()
        pw = Entry(top,show='*', width = 30)
        pw.bind("<Return>", submitf)
        pw.place(x = 110, y = 100)
        top.mainloop()
def check_value_exists3(value):
    # Execute a query to check if the value exists in the table
    cur.execute('select pcode from stock')
    fetch = cur.fetchall()
    pcodlist = [h[0] for h in fetch]
    if value in pcodlist:
        return 1
    else:
        return 0

def print_stock():
    cur.execute("select * from Stock")
    data = cur.fetchall()
    headers = ["Product Code", "Product Name", "Quantity", "Price"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)

def admin():
        time.sleep(2)
        passsword()
        if c==1:
            ech='y'
            while(ech=='y' or ech=='Y'):
              while True:
                print("________________________________")
                print("1) Add New Item") 
                print("2) Alter Stock Item Values") 
                print("3) Deleting an Item")
                print("4) Display All Items")
                print("5) View Purchase history")
                print("6) Change Password")
                print("7) Logout")
                print("________________________________")
                while True:
                    ech2 = input("Enter the choice: ")
                    if not ech2.isdigit():
                        print("Enter only numeric values.")
                        continue
                    ech2 = int(ech2)
                    if not (0 < ech2 < 8):
                        print("Enter choice only from 1 to 7.")
                        continue
                    break
                if ech2 == 1:
                    ch = 'y'
                    while ch == 'y' or ch == 'Y':
                        pcode = input("Enter the product code: ")
                        pname = input("Enter the product name: ")
                        while True:
                            pq = input("Enter the quantity: ")
                            if not pq.isdigit():
                                print("Enter only numeric values.")
                                continue
                            break
                        while True:
                            pp = input("Enter the product price: ")
                            cur.execute("update stock set price={} where pcode={}".format(pp,pcode))
                            cur.execute("UPDATE stock SET price = %s WHERE pcode = %s", (pp, pcode))
                            try:
                                pp = float(pp)  # Attempt to convert 'pp' to a floating-point number
                            except ValueError:
                                print("\nInvalid price value.")
                                continue
                            break
                        cur.execute("INSERT INTO stock (pname, quantity, price) VALUES (%s, %s, %s)", (pname, pq, pp))
                        con.commit()
                        print("Item added to inventory")
                        while True:
                            ch = input("Would you like to keep adding items to your inventory? (y/n)")
                            if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                print("Enter only \'y\' or \'n\'.")
                                continue
                            else:
                                break
                    ech = input("Do you want to continue working? Press y/n ")


                    
                elif(ech2==2):
                    while True:
                        print("(1) Change Item Name")
                        print("(2) Alter Item Price")
                        print("(3) Update Stock")
                        print("(4) Go back to main menu")
                        print("Enter choice:")
                        while True:
                            alch = input()
                            if not alch.isdigit():
                                print("Enter only numeric values.")
                                continue
                            elif not (0 < int(alch) < 5):
                                print("Choose options only from 1, 2, 3 and 4.")
                            else:
                                break

                        print_stock()
                        alch = int(alch)
                        if alch == 1:
                            ch = 'y'
                            while ch == 'y' or ch == 'Y':
                                print("Enter product code of item to change Name:")  
                                pcode = get_valid_value()
                                newname = input("Enter the new name of product: ")
                                cur.execute("update stock set price={} where pcode={}".format(pp,pcode))
                                cur.execute("UPDATE stock SET price = %s WHERE pcode = %s", (pp, pcode))
                                cur.execute("UPDATE stock SET pname = %s WHERE pcode = %s", (newname, pcode))
                                print("Item's name has been changed")
                                con.commit()
                                ch = input("Would you like to change the price of any other Item in the inventory? (y/n)")
                                while True:
                                    ch = input("Would you like to change the name of any other Item in the inventory? (y/n)")
                                    if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                        print("Enter only \'y\' or \'n\'.")
                                        continue
                                    else:
                                        break
                        elif alch == 2:
                            ch = 'y'
                            while ch == 'y' or ch == 'Y':
                                print("Enter product code of item to update price:")  
                                pcode = get_valid_value()
                                while True:
                                    pp = (input("Enter the new price of product: "))
                                    cur.execute("update stock set price={} where pcode={}".format(pp,pcode))
                                    cur.execute("UPDATE stock SET price = %s WHERE pcode = %s", (pp, pcode))
                                    try:
                                        pp = float(pp)  # Attempt to convert 'pp' to a floating-point number
                                        cur.execute("UPDATE stock SET price = %s WHERE pcode = %s", (pp, pcode))
                                        print("Item's price is updated")
                                        con.commit()

                                    except ValueError:
                                        print("\nInvalid price value.\nItem's price is not updated \nNumeric value should be entered for the price.\n")
                                        continue
                                    break

                                ch = input("Would you like to change the price of any other Item in the inventory? (y/n)")
                                while True:
                                    ch = input("Would you like to change the price of any other Item in the inventory? (y/n)")
                                    if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                        print("Enter only \'y\' or \'n\'.")
                                        continue
                                    else:
                                        break
                            ech=str(input("Do you want to continue working? Press y/n "))

                        elif alch==3:
                            ch = 'y'
                            while ch == 'y' or ch == 'Y':
                                print("Enter product code of item to update stock:")  
                                pcode = get_valid_value()
                                while True:
                                    pp = input("Enter the updated stock of product: ")
                                    cur.execute("update stock set price={} where pcode={}".format(pp,pcode))
                                    cur.execute("UPDATE stock SET price = %s WHERE pcode = %s", (pp, pcode))
                                    if not pp.isdigit():
                                        print("Enter only numeric values.")
                                        continue
                                    pp = int(pp)
                                    cur.execute("UPDATE stock SET quantity = quantity + %s WHERE pcode = %s", (pp, pcode))
                                    print("Item's stock is updated")
                                    con.commit()
                                    break

                                ch = input("Would you like to change the price of any other Item in the inventory? (y/n)")
                                while True:
                                    ch = input("Would you like to change the quantity of any other Item in the inventory? (y/n)")
                                    if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                        print("Enter only \'y\' or \'n\'.")
                                        continue
                                    else:
                                        break
                        elif alch==4:
                            break



                elif(ech2==3):
                    print_stock()
                    ch= 'y'
                    while ch == 'y' or ch == 'Y':
                        print("Enter product code to delete item from inventory:")
                        pcode=get_valid_value()
                        cur.execute("delete from stock where pcode={}".format(pcode))
                        con.commit()
                        print("Item Deleted from Inventory successfully")
                        ch = input("Would you like to delete any other Item in the inventory? (y/n)")
                        while True:
                            ch = input("Would you like to delete any other Item in the inventory? (y/n)")
                            if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                print("Enter only \'y\' or \'n\'.")
                                continue
                            else:
                                break
                    ech=str(input("Do you want to continue working? Press y/n "))

                    
                elif(ech2==4):
                    cur.execute("select * from Stock")
                    data = cur.fetchall()
                    headers = ["Product Code", "Product Name", "Quantity", "Price"]
                    table = tabulate(data, headers=headers, tablefmt="grid")
                    print(table)
                                        
                elif(ech2==5):
                    cur.execute("select * from purchase")
                    data = cur.fetchall()

                    headers = ["PURCHASED DATE", "PHONE NUMBER", "PRODUCT CODE", "TOTAL PRICE PURCHASED"]
                    table = tabulate(data, headers=headers, tablefmt="grid")
                    print(table)
                    while True:
                        print("(1) Total amount purchased by each customer")
                        print("(2) Order purchase history by latest purchases")
                        print("(3) Go Back To Main Menu")
                        while True:
                            mj = input("Enter the choice: ")
                            if not mj.isdigit():
                                print("Enter only numeric values.")
                                continue
                            mj = int(mj)
                            if not (0 < mj <=3):
                                print("Enter choice only from 1 to 3.")
                                continue
                            break
                        if mj == 1:
                            cur.execute("select phone_no, sum(total_purchased_amount) from purchase group by phone_no")
                            data = cur.fetchall()

                            headers = ["PHONE NUMBER", "TOTAL PRICE PURCHASED"]
                            table = tabulate(data, headers=headers, tablefmt="grid")
                            print(table)
                        elif mj==2:
                            cur.execute("select * from purchase order by purchased_date desc")
                            data = cur.fetchall()

                            headers = ["PURCHASED DATE", "PHONE NUMBER", "PRODUCT CODE", "TOTAL PRICE PURCHASED"]
                            table = tabulate(data, headers=headers, tablefmt="grid")
                            print(table)
                        elif mj==3:
                            break


                    #order by purchase date desc
                    #group by phone number

                    
                elif(ech2==6):
                    
                    def submit():
                        cur.execute("select * from login")
                        for i in cur:
                            user,password=i
                        op=oldpass.get()
                        np=newpass.get()
                        if password==op and op!=np:
                            cur.execute("update login set password='{}' where password='{}'".format(np,op))
                            con.commit()
                            messagebox.showinfo("Success!!","Password changed successfully")
                        elif password==op and op==np:
                            messagebox.showinfo("Try Again!!","Both the passwords cannot be the same")
                        else:
                            messagebox.showinfo("Access Denied!!","Entered password is incorrect, Please Try Again!")
                    top = Tk()
                    top.geometry("450x300")
                    display = Label(top,text = "Change Password",font=('Calibri',16)).place(x = 130,y = 20)
                    old_password = Label(top,text = "Old Password").place(x = 40,y = 60)
                    new_password = Label(top,text = "New Password").place(x = 40, y = 100)
                    submit_button = Button(top,text = "Submit",command=submit).place(x = 170, y = 130)
                    oldpass = Entry(top,show='*',width = 30)
                    oldpass.place(x = 150, y = 60)
                    newpass = Entry(top,show='*', width = 30)
                    def lbsubmit(event):
                        submit()
                    newpass.bind("<Return>", lbsubmit)
                    newpass.place(x = 150, y = 100)
                    top.mainloop()


                elif(ech2==7):
                    print("Thank you for using PharmaTech's software system")
                    time.sleep(3)
                    break
                elif(ech2>7):
                    print("Choose only with1in given choices!!")




def add_to_cart():
    cn2='y'
    cur.execute("select * from Stock")
    data = cur.fetchall()
    headers = ["Product Code", "Product Name", "Quantity", "Price"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)
    while(cn2=='y' or cn2=='Y'):
        print("Enter the product code you want to add in cart")
        product_code = get_valid_value()  #accepting the product code
        cur.execute("select quantity from stock where pcode={}".format(product_code))
        quantity_available = cur.fetchone()[0]
        if quantity_available == 0:
            print("Sorry.Currently unavailable.")
            break
        product_quantity=int(input("Enter the quantity of the Item chosen: "))#accepting the product quantity


        print(type(quantity_available))
        if product_quantity > quantity_available:
            print("Not enough quantity available.")
            while True:
                product_quantity=int(input("Enter a valid amount of quantity: "))
                if product_quantity < quantity_available:
                    break

        cur.execute("select price from stock where pcode={}".format(product_code))
        price=cur.fetchone()[0]
        cur.execute("select pname from stock where pcode={}".format(product_code))
        product_name=cur.fetchone()[0]
        con.commit()
        amount = price * product_quantity
        cur.execute("INSERT INTO cart VALUES({}, \"{}\", {}, {},{})".format(product_code, product_name, product_quantity,price, amount))
        con.commit()
        print("Product added to your cart.\n\n")
        cn2=input("do you want to continue adding products to your cart?(y/n)")
        while True:
            cn2 = input("do you want to continue adding products to your cart?(y/n)")
            if not (cn2.lower() == 'y' or cn2.lower() == 'n'):
                print("Enter only \'y\' or \'n\'.")
                continue
            else:
                break


def customer():
        conditioni='y'
        while(conditioni=='y' or conditioni=='Y'):
            print("________________________________")
            print("1.View Available Items")
            print("2. Add To Cart")
            print("3. View Cart")
            print("4: Delete Items from Cart")
            print("5. Print Bill")
            print("6: Exit Store")
            print("________________________________")


            ch9=input("Enter your choice: ")

            if(ch9=='1'):                                                               #VIEW AVAILABLE ITEMS
                cur.execute("select * from Stock")
                data = cur.fetchall()
                headers = ["Product Code", "Product Name", "Quantity", "Price"]
                table = tabulate(data, headers=headers, tablefmt="grid")
                print(table)

            
            
            elif(ch9=='2'):                                                             #ADD TO CART
                add_to_cart()


                    
            elif(ch9=='3'):                                                        #delete items from cart #before- View cart
                cur.execute("SELECT COUNT(*) FROM cart")
                count_results = cur.fetchall()

                # Extract the count value from the result
                count = count_results[0][0]
                if count != 0:
                    cur.execute(" SELECT pcode, pname, sum(quantity), price, sum(unit_price) FROM cart GROUP BY pcode, pname, price")
                    data = cur.fetchall()
                    print(data)
                    headers = ["PRODUCT CODE", "PRODUCT NAME", "QUANTITY", "UNIT PRICE","PRICE"]
                    table = tabulate(data, headers=headers, tablefmt="grid")
                    print(table)
                else:
                    print("YOU HAVEN'T ADDED ANYTHING TO YOUR CART. DO YOU WISH TO ADD ANYTHING? (y/n)")
                    cn3=input()
                    if cn3=='y':
                        add_to_cart()

            elif(ch9=='4'):
                cur.execute("SELECT pcode, pname, sum(quantity), price, sum(unit_price) FROM cart GROUP BY pcode, pname, price")
                data = cur.fetchall()


                if data:
                    headers = ["PRODUCT CODE", "PRODUCT NAME", "QUANTITY", "UNIT PRICE", "PRICE"]
                    table = tabulate(data, headers=headers, tablefmt="grid")
                    print(table)


                    ch = 'y'
                    while ch == 'y' or ch == 'Y':
                        print("Enter the product code of the item you want to remove from cart:")
                        pcode = get_valid_value()
                        cur.execute("delete from cart where pcode={}".format(pcode))
                        con.commit()
                        print("Item Deleted from cart successfully")
                        ch = input("Would you like to delete any other Item in your cart? (y/n)")

                        while True:
                            ch = input("Would you like to delete any other Item in your cart? (y/n)")
                            if not (ch.lower() == 'y' or ch.lower() == 'n'):
                                print("Enter only \'y\' or \'n\'.")
                                continue
                            else:
                                break
                else:
                    print("No items in cart to delete")


                            
            elif(ch9=='5'):#PRINT BILL

                while True:
                    cur.execute("SELECT COUNT(*) FROM cart")
                    count_results = cur.fetchone()

                    count = count_results[0]
                    if count == 0:
                        print("YOU HAVEN'T ADDED ANYTHING TO YOUR CART. DO YOU WISH TO ADD ANYTHING(y/n)")
                        nk=input()
                        if nk.lower()=='y':
                            cn2 = 'y'
                            cur.execute("select * from Stock")
                            data = cur.fetchall()
                            headers = ["Product Code", "Product Name", "Quantity", "Price"]
                            table = tabulate(data, headers=headers, tablefmt="grid")
                            print(table)
                            while (cn2 == 'y' or cn2 == 'Y'):
                                print("Enter the product code you want to add in cart")
                                product_code = get_valid_value()  # accepting the product code
                                cur.execute("select quantity from stock where pcode={}".format(product_code))
                                quantity_available = cur.fetchone()[0]
                                if quantity_available == 0:
                                    print("Sorry.Currently unavailable.")
                                    break
                                product_quantity = int(
                                    input("Enter the quantity of the Item chosen: "))  # accepting the product quantity

                                print(type(quantity_available))
                                if product_quantity > quantity_available:
                                    print("Not enough quantity available.")
                                    while True:
                                        product_quantity = int(input("Enter a valid amount of quantity: "))
                                        if product_quantity < quantity_available:
                                            break

                                cur.execute("select price from stock where pcode={}".format(product_code))
                                price = cur.fetchone()[0]
                                cur.execute("select pname from stock where pcode={}".format(product_code))
                                product_name = cur.fetchone()[0]
                                con.commit()
                                amount = price * product_quantity
                                cur.execute("INSERT INTO cart VALUES({}, \"{}\", {}, {},{})".format(product_code, product_name,product_quantity, price,amount))
                                con.commit()
                                print("Product added to your cart.\n\n")
                                cn2=input("do you want to continue adding products to your cart?(y/n)")
                                while True:
                                    cn2 = input("do you want to continue adding products to your cart?(y/n)")
                                    if not (cn2.lower() == 'y' or cn2.lower() == 'n'):
                                        print("Enter only \'y\' or \'n\'.")
                                        continue
                                    else:
                                        break


                            print("\n\nPROCEEDING TO PRINT THE BILL....\n\n")

                            time.sleep(3)


                            print("PLEASE PROVIDE THE DETAILS FOR THE FOLLOWING QUESTIONS")
                            name = input("Enter your name: ")
                            phone_number = input("Enter the customer's phone number: ")
                            while len(phone_number) != 10:
                                print("Please enter a valid phone number.")
                                phone_number = input("Enter the customer's phone number: ")

                            # Calculate total and fetch unit prices
                            total = 0
                            unit_prices = []
                            product_codes=[]
                            stock_quan=[]   #quantites that are in stock
                            updated_stock=[]
                            netot=[]

                            cur.execute("SELECT distinct pcode from cart")
                            rows = cur.fetchall()
                            cart_code = [row[0] for row in rows]

                            cur.execute("SELECT pname FROM cart GROUP BY pcode, pname, price")
                            rows1 = cur.fetchall()
                            cart_name0 = [row[0] for row in rows1]

                            for i in cart_name0:
                                cur.execute("INSERT INTO name VALUES('{}')".format(i))
                                con.commit()

                            cur.execute("SELECT pr_name FROM name")
                            rows6 = cur.fetchall()
                            cart_name1 = [row[0] for row in rows6]




                            cur.execute("SELECT price FROM cart GROUP BY pcode, pname, price")    #unit price
                            rows2 = cur.fetchall()
                            cart_unit = [row[0] for row in rows2]

                            cur.execute("SELECT sum(unit_price) FROM cart GROUP BY pcode, pname, price") #total price
                            rows3 = cur.fetchall()
                            cart_total = [row[0] for row in rows3]

                            cur.execute("SELECT sum(quantity) FROM cart GROUP BY pcode, pname, price")    #unit price
                            rows4 = cur.fetchall()
                            cart_quantity = [row[0] for row in rows4]   #list of values of quantities that the customer chose [2,3,2]

                            cur.execute("SELECT pcode FROM stock")
                            rows5 = cur.fetchall()
                            cart_name = [row[0] for row in rows5]

                            #quantity from stock, quantity from cart, [updated stock]
                            #1,2,3

                            for i in cart_code:
                                cur.execute("SELECT quantity from stock where pcode={}".format(i))
                                row_quan=cur.fetchone()[0]
                                quant=row_quan
                                stock_quan.append(quant)   #[150,130,40]

                            for i in range(len(cart_quantity)):
                                updated_stock.append(int(stock_quan[i]) - int(cart_quantity[i]))

                            for i in range(len(cart_code)):
                                cur.execute("update stock set quantity={} where pcode={}".format(updated_stock[i],cart_code[i]))


                            print("\n\n\nPRINTING THE BILL.....")
                            time.sleep(3)
                            # Print the bill
                            print("_" * 100)
                            print("                                                                      ")
                            print("                           \t\t\tBill To Be Paid\t\t\t                ")
                            print("_" * 100)
                            print("\n\n\n")
                            today = date.today()
                            d1 = today.strftime("%d/%m/%Y")
                            print("Date of billing:", d1)
                            print("Customer name:", name)
                            print("Contact number:", phone_number)
                            print("\n\n\n")
                            d2 = today.strftime('%Y-%m-%d')
                            cur.execute("SELECT COUNT(DISTINCT pcode) FROM cart")
                            count_results = cur.fetchone()
                            count = count_results[0]
                            main_list = []

                            for i in range(len(cart_code)):
                                cur.execute("INSERT INTO purchase (purchased_date, phone_no, pcode, total_purchased_amount) VALUES (%s, %s, %s, %s)",(d2, phone_number, cart_code[i], cart_total[i]))
                                con.commit()






                            for i in range(count):

                                main_list.append([str(cart_name1[i]),cart_quantity[i],cart_unit[i],cart_total[i]])

                            headers = ["DESCRIPTION", "QUANTITY", "UNIT PRICE(₹)", "TOTAL(₹)"]

                            table = tabulate(main_list, headers=headers, tablefmt="grid")

                            print(table)
                            print("\n\n\n")
                            print("TOTAL AMOUNT TO BE PAID:              ₹", sum(cart_total),"-/")
                            print("\n")
                            print("-"*100)
                            cur.execute("delete from cart")
                            cur.execute("delete from name")
                            con.commit()
                            print("\t\t\t\t\tTHANK YOU FOR CHOOSING PHARMAHUB\n\t\t\t\t\t\tGET WELL SOON!!")  
                            break
                        else:
                            break
                    else:
                        print("PLEASE PROVIDE THE DETAILS FOR THE FOLLOWING QUESTIONS")
                        name = input("Enter your name: ")
                        phone_number = input("Enter the customer's phone number: ")
                        while len(phone_number) != 10:
                            print("Please enter a valid phone number.")
                            phone_number = input("Enter the customer's phone number: ")

                        # Calculate total and fetch unit prices
                        total = 0
                        unit_prices = []
                        product_codes = []
                        stock_quan = []  # quantites that are in stock
                        updated_stock = []
                        netot = []

                        cur.execute("SELECT distinct pcode from cart")
                        rows = cur.fetchall()
                        cart_code = [row[0] for row in rows]

                        cur.execute("SELECT pname FROM cart GROUP BY pcode, pname, price")
                        rows1 = cur.fetchall()
                        cart_name0 = [row[0] for row in rows1]

                        for i in cart_name0:
                            cur.execute("INSERT INTO name VALUES('{}')".format(i))
                            con.commit()

                        cur.execute("SELECT pr_name FROM name")
                        rows6 = cur.fetchall()
                        cart_name1 = [row[0] for row in rows6]

                        cur.execute("SELECT price FROM cart GROUP BY pcode, pname, price")  # unit price
                        rows2 = cur.fetchall()
                        cart_unit = [row[0] for row in rows2]

                        cur.execute("SELECT sum(unit_price) FROM cart GROUP BY pcode, pname, price")  # total price
                        rows3 = cur.fetchall()
                        cart_total = [row[0] for row in rows3]

                        cur.execute("SELECT sum(quantity) FROM cart GROUP BY pcode, pname, price")  

                        rows4 = cur.fetchall()
                        cart_quantity = [row[0] for row in
                                         rows4]  # list of values of quantities that the customer chose [2,3,2]

                        cur.execute("SELECT pcode FROM stock")
                        rows5 = cur.fetchall()
                        cart_name = [row[0] for row in rows5]

                        # quantity from stock, quantity from cart, [updated stock]
                        # 1,2,3

                        for i in cart_code:
                            cur.execute("SELECT quantity from stock where pcode={}".format(i))
                            row_quan = cur.fetchone()[0]
                            quant = row_quan
                            stock_quan.append(quant)  # [150,130,40]

                        for i in range(len(cart_quantity)):
                            updated_stock.append(int(stock_quan[i]) - int(cart_quantity[i]))

                        for i in range(len(cart_code)):
                            cur.execute("update stock set quantity={} where pcode={}".format(updated_stock[i], cart_code[i]))

                        print("\n\n\nPRINTING THE BILL.....")
                        time.sleep(3)
                        # Print the bill
                        print("_" * 100)
                        print("                                                                      ")
                        print("                           \t\t\tBill To Be Paid\t\t\t                ")
                        print("_" * 100)
                        print("\n\n\n")
                        today = date.today()
                        d1 = today.strftime("%d/%m/%Y")
                        print("Date of billing:", d1)
                        print("Customer name:", name)
                        print("Contact number:", phone_number)
                        print("\n\n\n")
                        d2 = today.strftime('%Y-%m-%d')
                        cur.execute("SELECT COUNT(DISTINCT pcode) FROM cart")
                        count_results = cur.fetchone()
                        count = count_results[0]
                        main_list = []

                        for i in range(len(cart_code)):
                            cur.execute(
                                "INSERT INTO purchase (purchased_date, phone_no, pcode, total_purchased_amount) VALUES (%s, %s, %s, %s)",
                                (d2, phone_number, cart_code[i], cart_total[i]))
                            con.commit()

                        for i in range(count):
                            main_list.append([str(cart_name1[i]), cart_quantity[i], cart_unit[i], cart_total[i]])

                        headers = ["DESCRIPTION", "QUANTITY", "UNIT PRICE(₹)", "TOTAL(₹)"]

                        table = tabulate(main_list, headers=headers, tablefmt="grid")

                        print(table)
                        print("\n\n\n")
                        print("TOTAL AMOUNT TO BE PAID:              ₹", sum(cart_total), "-/")
                        print("\n")
                        print("-" * 100)
                        cur.execute("delete from cart")
                        cur.execute("delete from name")
                        con.commit()
                        print("\t\t\t\t\tTHANK YOU FOR CHOOSING PHARMAHUB\n\t\t\t\t\t\tGET WELL SOON!!")  
                        break


            elif(ch9=='6'):
                print("\n\n\t\t\t\t\t\tTHANK YOU FOR VISITING PHARMAHUB!")
                break
                
            else:
                print("PLEASE CHOOSE WITHIN GIVEN OPTIONS!!")
            
print("_"*100)
print("                                                                                                                                                 ")
print("                                         WELCOME TO PHARMAHUB                                    ")
print("                                                                                                                                                 ")
print("_"*100)
        
while True:
    print("________________________________")
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    print("________________________________")
    while True:
        ch=input("Enter the choice: ")
        if not ch.isdigit():
            print("Enter numeric values only")
            continue
        ch = int(ch)
        if not (0 < ch < 4):
            print("Enter choice only from 1 to 3")
            continue
        else:
            break
    if ch==1:
        admin()
    elif ch==2:
        customer()
        break
    elif ch==3:
        print("\nEXITING")
        time.sleep(1)
        print("PharmaTech.tech")
        break
    else:
        print("Enter only within given choices!!")
        continue
    

cur.close()
con.close()
