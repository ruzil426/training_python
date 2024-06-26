class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors or self.buildingType == other.buildingType

number1 = (1, 'Частный дом')
number2 = (10, 'МКД')
print(number1 != number2)