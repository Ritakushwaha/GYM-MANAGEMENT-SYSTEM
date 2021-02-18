from Package_DAO import Package_dao
from database_connectivity import MyDB
from Customer_DAO import Customer_dao


customer_dao = Customer_dao()
package_dao = Package_dao()
mydb = MyDB()
package_dao.create_package()
customer_dao.create_customer()


print ("\n")
print ("*****GYM MANAGEMENT SYSTEM*****")

def menu():
    print ("1. Add Package")
    print ("2. Add Customer")
    print ("3. Show all packages")
    print ("4. Show all customers")
    print ("5. Find customer details by name")
    print ("6. Show this menu again")
    print ("7. Update customer package,subscription and payment details")
    print ("8. Exit")
    print ("Enter  Choice: ")

def input_ph_no():
    mob_num = str(input("Enter customer's mobile no. - "))
    mob_n =  validate_phone_no(mob_num)
    return mob_n

def validate_phone_no(mob_num):
    ph_num = mob_num
    if ph_num.isdigit() and len(ph_num) == 10:
        return ph_num
    else:
        print("Please, Enter valid Mobile No.")
        input_ph_no()

def input_package():
    pack_type = package_dao.show_package_type()
    print(pack_type)
    inp_pack = str(input("Choose Package - "))
    inp_p = validate_package(inp_pack,pack_type)
    return inp_p

def validate_package(inp_p, p_type):
    pack_type = p_type.split()
    inp_pack = inp_p.upper()
    if inp_pack in pack_type:
        return inp_pack
    else:
        print("Please, choose a valid package type.")
        input_package()

def input_subscription():
    sub_type = package_dao.show_subscription()
    print(sub_type)
    inp_subs = str(input("Choose Subscription - "))
    inp_s =  validate_subscription(inp_subs,sub_type)
    return inp_s

def validate_subscription(inp_s, s_type):
    sub_type = s_type.split()
    inp_subs = inp_s.upper()
    if inp_subs in sub_type:
        return inp_subs
    else:
        print("Please, choose a valid subscription type.")
        input_subscription()

def input_customer_id():
    inp_id = str(input("Enter Customer ID - "))
    cust_id = validate_cust_id(inp_id)
    return cust_id

def validate_cust_id(inp_id):
    if customer_dao.check_cust_id(inp_id):
        print(inp_id + " inp_id")
        return inp_id
    else:
        print("Please enter valid customer id")
        x = input_customer_id()
        return x

menu()

while(True):
    inp = int(input())
    if inp == 2:
        customer = []
        name = str(input("Enter customer's name - "))
        mob_no = input_ph_no()
        package_type = input_package()
        subscription = input_subscription()
        payment = str(input("Amount Paid - "))

        customer.append(name)
        customer.append(mob_no)
        customer.append(package_type)
        customer.append(subscription)
        customer.append(payment)
        customer_dao.add_customer(customer)
        customer_dao.generate_receipt(name)

    elif inp == 1:
        package = []
        type = str(input("Enter package type - "))
        subscription = str(input("Enter subscription type - "))
        facilities = str(input("Enter facilities - "))
        cost = str(input("Enter package cost - "))
        package.append(type)
        package.append(subscription)
        package.append(facilities)
        package.append(cost)
        package_dao.add_package(package)

    elif inp == 3:
        package_dao.show_package()

    elif inp == 4:
        customer_dao.show_customer()

    elif inp == 5:
        cust_name = str(input("Enter Customer name - "))
        customer_dao.show_customer_by_name(cust_name)

    elif inp == 6:
        menu()

    elif inp == 8:
        exit(0)

    elif inp == 7:
        cust_id = input_customer_id()
        print("cust_id")
        print(cust_id)
        package_type = input_package()
        subscription = input_subscription()
        payment = str(input("New Amount Paid - "))
        customer = []

        customer.append(package_type)
        customer.append(subscription)
        customer.append(payment)
        customer.append(cust_id)

        customer_dao.update_details(customer)
        cust_name = customer_dao.get_name(cust_id)
        customer_dao.generate_receipt(cust_name)

    else:
        print ("Please choose a valid option")
    menu()
