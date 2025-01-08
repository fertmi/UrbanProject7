from re import search


class Product: # Product('Potato', 50.0, 'Vagetables')
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self. category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_products = file.read()
        file.close()
        return file_products

    def add(self, *products):
        file_products = self.get_products()
        for i in range(len(products)):
            # file_products = self.get_products()
            if search(products[i].name, file_products):
                print(f'Продукт {products[i].name} уже есть в магазине')
                continue
            file = open(self.__file_name, 'a')
            file.write(str(products[i]))
            file.write('\n')
            file.close()

#Основаная программа
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())