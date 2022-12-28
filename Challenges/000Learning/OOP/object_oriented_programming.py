string = 'hello'
print(string.upper())  #  when you have a . after an object that is a method
                       #  which is basically something that affects the obj

class Item:  #  Instance means the same thing
    #  inside our class is where we design methods that will be allowed to be executed on our instances
    def __init__(self):

        print('I AM CREATED')


    def calculate_total_price(self, x, y):  # here we create a METHOD, a function inside a class
        return x * y
        #  SELF is automatically inside the brackets because Python calls
        #  the object itself as a first argument when you call the methods


    pass

item1 = Item()  #  created an instance of the class
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))  # (self, x, y) == (item1, price, quantity)



item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))