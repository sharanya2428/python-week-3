class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        total = 0
        print("Product\tPrice\tQty\tAmount")

        for p in self.products:
            amount = p.total()
            print(p.name, p.price, p.quantity, amount, sep="\t")
            total += amount

        tax = total * 0.05
        print("Total:", total)
        print("Tax (5%):", tax)
        print("Final Bill:", total + tax)


p1 = Product("Pen", 10, 5)
p2 = Product("Book", 50, 2)

bill = Bill()
bill.add_product(p1)
bill.add_product(p2)
bill.display_bill()
