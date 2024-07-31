from pprint import pprint
class Shop:
    __file_name = 'products.txt'
    def __init__(self):
        pass
    def get_products(self):
        self.file_read = open(self.__file_name, 'r')
        self.content = self.file_read.read()
        self.file_read.close()
        return self.content
    def add(self, *products):
        # self.get_products()
        self.file_append = open(self.__file_name, 'a')
        for product in products:
            if product.name not in self.get_products():
                self.file_append.write(str(product) + '\n')
                self.file_append.seek(0)
            else:
                print(f' Продукт {product.name} уже есть в магазине')

        self.file_append.close()
        # for line in file:
        #     if products in line: #!= self.str(*products):
        #         self.__file_name.append(*products)
        # else:
        #     print(f'{self.str(*products)} уже есть в магазине')
        # file.close()
class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())