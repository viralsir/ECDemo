from Order import Order
from util_lib import display_menu

arham={"Vendor":[],"Customer":[]}
main_menu=["Purchase","Sales","Exit"]
sub_menu=["Entry","View","Main Menu"]


def billing(title,key):
    op2 = 0
    while op2 != sub_menu.index("Main Menu"):

        op2 = display_menu(op_list=sub_menu, title=title)

        if op2 == sub_menu.index("Entry"):
            op3 = "yes"
            while op3.lower() == "yes":
                order = Order()
                order.setOrder(title=key)
                arham[key].append(order)
                op3 = input("Do you want to add another Bill?(yes/no):")
        elif op2 == sub_menu.index("View"):
            print("\t\t View ")
            for order in arham[key]:
                order.getOrder(title=key)
                print("===========================")
        elif op2 == sub_menu.index("Main Menu"):
            print("Back to the main menu")
        else:
            print("wrong option selected try again !!!")



op1=0
while op1 != main_menu.index("Exit"):
    op1=display_menu(op_list=main_menu,title="Arham Pvt Ltd")

    if op1==main_menu.index("Purchase"):
        billing(title="Purchase",key="Vendor")
    elif op1==main_menu.index("Sales"):
        billing(title="Sales",key="Customer")
    elif op1==main_menu.index("Exit"):
        print("You are Exited ")
    else :
        print("Wrong option selected try again !!")

