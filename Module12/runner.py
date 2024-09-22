class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        # print(self.distance)

    def walk(self):
        self.distance += 5
        # print(self.distance)

    def __str__(self):
        return self.name

# r1 = Runner('Bob')
# r1.run()
# r1.walk()
