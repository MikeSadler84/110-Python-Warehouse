

# This is how to create an object


class Item:
    id = 0
    title = ""
    category = ""
    stock = 0
    price = 0.0

    # always use self first, after that you can do it in any order

    def __init__(self, id, title, category, stock, price):
        self.id = id
        self.title = title
        self.category = category
        self.stock = stock
        self.price = price
