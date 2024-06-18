class House:
    def __init__(self):
        self.numberOfFloors = 0
        print(self.numberOfFloors)

    def setNewNumberOfFloors(self, floors):
        #floors = 3
        #print(self.numberOfFloors)
        self.numberOfFloors = floors
        print(self.numberOfFloors)


floor1 = House()
floor1.setNewNumberOfFloors(3)
