from util_lib import  is_nagetive
class Product:
    id=0
    name=""
    qty=0
    rate=0
    price=0

    def setProduct(self):
        self.id=is_nagetive(int(input("Enter Product Id :")),title="Id :")
        self.name=input("Enter Product Name :")
        self.qty=is_nagetive(int(input("Enter Product Qty :")),title="Qty :")
        self.rate=is_nagetive(float(input("Enter Product Rate:")),title="Rate:")
        self.price=self.qty*self.rate

    def getProduct(self):
        print(str(self.id).ljust(10)
              ,self.name.ljust(10)
              ,str(self.qty).ljust(10),
              str(self.rate).ljust(10)
              ,str(self.price).ljust(10))
