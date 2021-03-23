from Vendor import Vendor
from Customer import Customer
from util_lib import display_menu

Vendor_List=[]
Customer_List=[]
main_menu=["Purchase","Sales","Exit"]
sub_menu=["Entry","View","Main Menu"]
op1=0
while op1 != main_menu.index("Exit"):
    op1=display_menu(op_list=main_menu,title="Arham Pvt Ltd")

    if op1==main_menu.index("Purchase"):
        op2=0
        while op2 != sub_menu.index("Main Menu"):

            op2=display_menu(op_list=sub_menu,title="Purchase")

            if op2==sub_menu.index("Entry"):
                op3="yes"
                while op3.lower()=="yes":
                    vendor=Vendor()
                    vendor.setVendor()
                    Vendor_List.append(vendor)
                    op3=input("Do you want to add another Bill?(yes/no):")
            elif op2==sub_menu.index("View"):
                print("\t\t View ")
                for vendor in Vendor_List:
                    vendor.getVendor()
                    print("===========================")
            elif op2==sub_menu.index("Main Menu"):
                print("Back to the main menu")
            else :
                print("wrong option selected try again !!!")
    elif op1==main_menu.index("Sales"):
        op2 = 0
        while op2 != sub_menu.index("Main Menu"):
            op2 = display_menu(op_list=sub_menu, title="Sales")

            if op2 == sub_menu.index("Entry"):
                op3 = "yes"
                while op3.lower() == "yes":
                    customer=Customer()
                    customer.setCustomer()
                    Customer_List.append(customer)
                    op3 = input("Do you want to add another Bill?(yes/no):")
            elif op2 == sub_menu.index("View"):
                print("\t\t View ")
                for customer in Customer_List:
                    customer.getCustomer()
                    print("===========================")
            elif op2 == sub_menu.index("Main Menu"):
                print("Back to the main menu")
            else:
                print("wrong option selected try again !!!")

    elif op1==main_menu.index("Exit"):
        print("You are Exited ")
    else :
        print("Wrong option selected try again !!")

