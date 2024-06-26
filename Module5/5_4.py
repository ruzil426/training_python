class Building:
    total = 0

    def __init__(self):
        self.total
        self.plus()

    def plus(self):
        for i in range(40):
            self.total += 1
            print(f'Дом {self.total}')

house = Building()