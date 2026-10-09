class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 0.05

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        subtotal = sum(p.get_total() for p in self.products)
        tax = subtotal * self.tax_rate
        total = subtotal + tax

        print("\n========== BILL ==========")
        print(f"{'Product':<15}{'Price':>8}{'Qty':>6}{'Total':>10}")
        print("-" * 39)

        for p in self.products:
            print(f"{p.name:<15}{p.price:>8.2f}"
                  f"{p.quantity:>6}{p.get_total():>10.2f}")

        print("-" * 39)
        print(f"{'Subtotal:':>29} {subtotal:.2f}")
        print(f"{'Tax (5%):':>29} {tax:.2f}")
        print(f"{'Final Total:':>29} {total:.2f}")
        print("===========================")


bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()
