class fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def describe(self):
        print(f'This is a {self.name}, they are usually {self.color}')

apple = fruit('apple', 'red', 1)
banana = fruit('banana', 'yellow', 3)
kiwi = fruit('kiwi', 'green', 5)

apple.describe()
banana.describe()
kiwi.describe()