class Personal:
    name=""
    address=""
    phno=""

    def setPersonal(self,title):
        self.name=input("Enter "+title+" Name :")
        self.address=input("Enter "+title+" Address:")
        self.phno=input("Enter "+title+" Phno:")


    def getPersonal(self,title):
        print(title," Name :",self.name)
        print(title," Address:",self.address)
        print(title," Phno:",self.phno)
