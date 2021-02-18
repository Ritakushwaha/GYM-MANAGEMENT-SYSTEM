from database_connectivity import MyDB
from mysql.connector import Error
from datetime import date

mydb = MyDB()

class Package_dao:
    def create_package(self):
        try :
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            self.cur.execute('''CREATE TABLE if not exists Package(id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(100) not null, subscription varchar(10) constraint check(subscription = 'MONTHLY' or subscription = 'YEARLY' or subscription = 'QUARTERLY' or subscription = '6 MONTHS'), facilities VARCHAR(500) not null, cost double not null)''')
            conn.commit()
        except Error as e:
            print("Error while creating Customer",e)

    def add_package(self,package_list):
        _type = package_list[0].upper()
        _subscription = package_list[1].upper()
        _facilities = package_list[2].upper()
        _cost = package_list[3]
        try:
            conn = mydb.get_connection()
            self.cur = conn.cursor()
            ins_qry = '''INSERT INTO Package (type, subscription,facilities, cost) values (%s, %s, %s, %s)'''
            ins_values = (_type, _subscription, _facilities, _cost)
            self.cur.execute(ins_qry,ins_values)
            conn.commit()
        except Error as e:
            print("Error while adding package",e)

    def show_package_type(self):
        try:
            conn = mydb.get_connection()
            sql_select_Query = "select distinct type from Package"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Package Type")
            pack = ""
            for row in records :
                str = "".join(row[0])
                pack += str+"\n"
            return pack
        except Error as e:
            print("Error reading data from MySQL table", e)

    def show_subscription(self):
        try:
            conn = mydb.get_connection()
            sql_select_Query = "select distinct subscription from Package"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("Subscription")
            subs= ""
            for row in records :
                str = "".join(row[0])
                subs += str + "\n"
            return subs
        except Error as e:
            print("Error reading data from MySQL table", e)

    def show_package(self):
        try:
            conn = mydb.get_connection()
            sql_select_Query = "select * from Package"
            cursor = conn.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            print("PackageID\tType\tSubcription\tFacilities\tCost")
            for row in records :
                print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\n')
        except Error as e:
            print("Error reading data from MySQL table", e)
