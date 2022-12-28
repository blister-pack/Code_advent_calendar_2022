import csv


string = 'hello'
print(string.upper())

#  REMEMBER class attributes are different from instance attributes
class Item:
    pay_rate = 0.8  #  pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):

        #  Run validations to the received arguments (it's a way to ensure the program runs the way it
        #  should, in this case price and quantity should be above 0
        assert price >= 0, f'Price {price} is not greater or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero!'

        #  Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
        '''
        after self you can pass other arguments that are necessary to create instances of a class (objects)
        that way it is no longer necessary to hard code everything the way we did in the other program
        if no quantity is passed in the instance, it assumes it's 0
        however, a quantity can still be passed in the instance itself without any problem
        '''

    def calculate_total_price(self):  # here we create a METHOD, a function inside a class
        return self.price * self.quantity
        #  SELF is automatically inside the brackets because Python calls
        #  the object itself as a first argument when you call the methods
        '''
        we don't need to define 3 arguments after we make the init
        we already have exactly what we need in the class itself
        '''

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            '''creates a dict from the csv, not sure I understand this'''
        '''needs to be converted into a class method because there are
        no instances to call this from, since this method is literally
        designed to create instances - we use a decorator for that'''


    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'
        #  this makes our ALL list way more friendly to read
        #  It's best practice to have the instances returned in the same way we create them
        #  We can just copy and paste stuff to our console, it's returned the same way we write it


Item.instantiate_from_csv()