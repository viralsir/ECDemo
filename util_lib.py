def is_nagetive(value,title):
    while value<0:
        print("nagetive value are not allowed")
        value=float(input("Enter "+title))
    return value;

def display_menu(op_list,title):
    print("\t\t\t",title)
    for i in range(len(op_list)):
        print("\t\t press ",i ," for ",op_list[i])

    op=is_nagetive(int(input("Enter Your option :")),title="you option:")
    return op;

