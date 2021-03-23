from Personal_Info import Personal
from Product_Info import Product
from util_lib import is_nagetive
class Order(Personal):
    billid=0
    billdate=""
    Product_List=""
    totalamount=0
    discount=0
    gst=0
    netamount=0

    def setOrder(self,title):
        self.billid=is_nagetive(int(input("Enter Bill Id:")),title="Bill Id:")
        self.billdate=input("Enter Bill Date :")

        self.setPersonal(title=title)
        self.Product_List=[]
        op="yes"
        while op.lower()=="yes":
            product=Product()
            product.setProduct()
            self.totalamount += product.price
            self.Product_List.append(product)
            op=input("Do you want to Add another Product(yes/no)?:")

        self.discount=is_nagetive(float(input("Enter Discount(%):")),title="Discount :")
        self.discount=(self.discount*self.totalamount)/100
        self.gst =is_nagetive(float(input("Enter GST(%):")),title="GST:")
        self.gst = (self.gst * self.totalamount) / 100
        self.netamount=self.totalamount-self.discount+self.gst

    def getOrder(self,title):
        print("Bill Id :",self.billid)
        print("Bill Date:",self.billdate)

        self.getPersonal(title=title)

        print("id".ljust(10),
              "Name".ljust(10),
              "Qty".ljust(10),
              "Rate:".ljust(10),
              "Price".ljust(10))
        for product in self.Product_List:
            product.getProduct()

        print("Total Amount :",self.totalamount)
        print("Discount :",self.discount)
        print("GST:",self.gst)
        print("Net Amount :",self.netamount)


