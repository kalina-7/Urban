class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop(Product):
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name


    def get_products(self):
        f = open(self.__file_name, 'r')
        product = f.read()
        f.close()
        return product


    def add(self, *products):
        f = open(self.__file_name, 'a')
        new_products = self.get_products()
        for p in products:
            if p.name not in new_products:
                f.write(str(p))
                f.write('\n')
            else:
                print(f'Продукт {p} уже есть в магазине')
        f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())