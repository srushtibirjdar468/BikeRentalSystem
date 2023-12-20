class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value")
        elif q>self.stock:
            Print("Enter the value (less than stock)")
        else:
             self.stock=self.stock-q
             print("Total prices",q*100)
             print("Total Bikes",self.stock)

while True:
    obj=BikeShop(100)
    uc=int(input(
'''
1.Display stoccks
2.Rent a Bike
3.Exit
'''
        ))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the qty:--"))
        obj.rentForBike(n)
    else:
        break
