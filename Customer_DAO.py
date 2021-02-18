from database_connectivity import MyDB
from Package_DAO import Package_dao
from mysql.connector import Error
from datetime import date

#object of MyDB class
mydb = MyDB()

class Customer_dao:
    # Create Customer table in database 'gym_manager'
    def create_customer(self):
        try :
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            self.cur.execute('''CREATE TABLE if not exists Customer(
                id INT not null AUTO_INCREMENT PRIMARY KEY, 
                name VARCHAR(100) not null, 
                phoneNo BIGINT(10) not null, 
                joindate DATE, 
                package_type varchar(50) not null references Package(type), 
                subscription varchar(10) not null references Package(subscription), 
                payment double not null)''')
            conn.commit()
        except Error as e:
            print("Error while creating Customer",e)
            print(Style.RESET_ALL)

    def add_customer(self,customer_list):
        _cust_name = customer_list[0].upper()
        _phone_no = customer_list[1]
        _package_type = customer_list[2]
        _subscription = customer_list[3]
        _payment = customer_list[4]
        try:
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            distinct_type = '''select distinct type from Package'''
            distinct_subscription = '''select distinct subscription from Package'''
            self.cur.execute(distinct_type)
            records = self.cur.fetchall()
            print(records)
            self.cur.execute(distinct_subscription)
            records1 = self.cur.fetchall()
            if ( any(_package_type in row for row in records )):
                if(any(_subscription in row1 for row1 in records1)):
                    ins_qry = "INSERT INTO Customer (name,phoneNo,joindate,package_type,subscription,payment) values(%s,%s,%s,%s,%s,%s)"
                    ins_values = (_cust_name,_phone_no,date.today(),_package_type,_subscription,_payment)
                    self.cur.execute(ins_qry,ins_values)
                else:
                    print("Subscription is invalid")
            else:
                print("Package not available")
            conn.commit()
        except Error as e:
            print("Error while adding customer",e)

    def show_customer(self):
        try:
            conn = mydb.get_connection()
            sql_select_Query = "select * from Customer"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("CustomerID       Name        Phone       Joining_Date        Package_type        Subscription        Payment")
            string = "{}      {}      {}      {}      {}      {}        {}\n"
            for row in records :
                print(string.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        except Error as e:
            print("Error reading data from MySQL table", e)

    def generate_receipt(self,_cust_name):
        try :
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = "SELECT * from Customer where name = %s"
            cust_name = (_cust_name.upper(),)
            self.cur.execute(qry, cust_name)
            records = self.cur.fetchall()
            if records == [] :
                print("User not found")
            else :
                #print("CustomerID\tName\tPhone\tJoining_Date\tPackage_type\tSubscription\tPayment")
                string = '''
                            _______________________________________________________\n
                                                HEALTHY GYM                        \n
                            __________Address: Near Bypass, Mandideep______________\n
                            Receipt no.   : {}00                                   \n
                            Customer ID   : {}                                     \n
                            Name          : {}                                     \n
                            Joining date  : {}                                     \n
                            Package       : {}                                     \n
                            Subscription  : {}                                     \n
                            Paid Amount   : {}                                     \n
                            _______________________________________________________\n
                                   For more details - Contact - 9111159292         \n 
                                         Stay connected, Stay Healthy              \n'''
                for row in records :
                    print("Customer's Receipt")
                    print(string.format(row[0],row[0],row[1],row[3],row[4],row[5],row[6]))
        except Error as e :
            print("Error while reading data ", e)

    def show_customer_by_name(self,_cust_name):
        try:
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = "SELECT * from Customer where name = %s"
            cust_name = (_cust_name.upper(),)
            self.cur.execute(qry,cust_name)
            records = self.cur.fetchall()
            if records == []:
                print("User not found")
            else:
                print("CustomerID\tName\tPhone\tJoining_Date\tPackage_type\tSubscription\tPayment")
                for row in records:
                    print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t',row[6],'\n')
        except Error as e:
            print("Error while reading data ",e)

    def check_cust_id(self, cust_id) :
        try :
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = "SELECT id from Customer where id = %s"
            _cust_id = (cust_id,)
            self.cur.execute(qry, _cust_id)
            records = self.cur.fetchall()
            print(records)
            if records != [] :
                print("ID Found")
                return True
            else :
                print("ID not found")
                return False
        except Error as e :
            print("Error while reading data ", e)

    def update_details(self,customer_list):
        try:
            _package_type = customer_list[0]
            _subscription = customer_list[1]
            _new_payment = customer_list[2]
            _cust_id = customer_list[3]

            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = '''update customer 
            set joindate = %s, 
            package_type= %s, 
            subscription = %s, 
            payment = %s 
            where id = %s'''
            values = (date.today(),_package_type,_subscription,_new_payment,_cust_id)
            self.cur.execute(qry,values)
            conn.commit()
        except Error as e:
            print("Error while reading data ", e)

    def get_name(self,cust_id):
        try :
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = "SELECT name from Customer where id = %s"
            _cust_id = (cust_id,)
            self.cur.execute(qry, _cust_id)
            records = self.cur.fetchall()
            print(records)
            if records != [] :
                for row in records :
                    str = row[0]
                return str
            else :
                print("Enter Valid customer id")
        except Error as e :
            print("Error while reading data ", e)


    '''def check_cust_id(self,cust_id):
        try:
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            qry = "SELECT * from Customer where id = %s"
            _cust_id = (cust_id,)
            self.cur.execute(qry, _cust_id)
            records = self.cur.fetchall()
            print(records)
            if records != [] :
                return True
            else :
                return False
        except Error as e:
            print("Error while reading data ", e)
'''




