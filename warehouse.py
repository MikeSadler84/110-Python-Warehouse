"""
Program: Warehouse control
Author: Mike Sadler
Functionality:
    - Register Items
        - id (auto generated): int
        - title: string
        - category: str
        - stock: int
        - price: float

"""

# import

from menu import print_menu, clear, print_item, print_header
from item import Item
import logging
import pickle  # serializer to store objects in files

# global vars
catalog = []
change_log = []
last_id = 1  # variable for starting ID
data_file = "warehouse.data"

# functions


def registered_item():
    global last_id  # have to import the simple variable into a function to stop the error
    try:
        print_header("Register New Item")
        title = input("Please provide the title: ")
        category = input("Please provide the category: ")
        stock = int(input("Please provide the amount in stock: "))
        price = float(input("Please provide the price: "))

        new_item = Item(last_id, title, category, stock, price)
        last_id += 1  # increases the variable +1 with each new item
        # Add the object to the list
        # print(new_item.title) how to read from the object
        catalog.append(new_item)

        # this is how you get the length of an array in Python
        count = len(catalog)
        print("Item saved! You have " + str(count) + " items in the catalog.")
    except ValueError:
        print("Error, please provide a valid number")
    except:
        print("Error, ensure the data is correct")


def serialize_catalog():
    global data_file
    # first part is the file name, wb = write binary which creates/overwrites the file
    writer = open(data_file, "wb")
    # dump = put array catalog into the writer file
    pickle.dump(catalog, writer)
    writer.close()
    print("Data saved!")

# exception handling try: and except:


def deserialize_catalog():
    global data_file, last_id
    try:
        # rb = read binary, allows you to read the file, will crash the system if the file doesn't exist
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]  # index -1 is the last item in an arry(list)
        last_id = last.id + 1
        how_many = len(catalog)
        print("Deserialized " + str(how_many) + " items")

    except:
        print("Error, no data loaded!")


def display_catalog():

    print_header("Your Catalog")
    for item in catalog:
        print_item(item)


def out_stock_item():
    print("Items out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)


def stock_value():
    print("Total stock value")
    stock_value = 0.00
    for item in catalog:
        stock_value += float(item.price) * float(item.stock)
        print("Your stock value is: $" + str(stock_value))


def update_price():
    print("Choose the item you wish to update")
    display_catalog()
    id = input("Choose the id you want to edit: ")
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            print("Updating " + item.title)
            new_price = input("Enter the new price: ")
            print("The new price of " + str(item.title) + " is " + new_price)
            item.price = new_price
    if(not found):
        print("Error, invalid ID. Try again.")


def delete_item():
    print("Choose the item you wish to delete")
    display_catalog()
    id = input("Choose the id you want to delete: ")
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            verify_delete = input(
                "Input [1] to verify you want to delete the " + item.title + ". Input any other key to cancel: ")
            if(verify_delete == "1"):
                print(item.title + " has been deleted")
                catalog.pop(int(id) - 1)
            else:
                print(item.title + " has not been deleted")
    if(not found):
        print("Error, invalid ID. Try again.")


def display_categories():

    print_header("Your Categories")
    # How to get unique categories so there are no duplicates
    temp_list = []
    for item in catalog:
        if(item.category not in temp_list):
            temp_list.append(item.category)
            print(item.category)


def update_stock():
    print("Choose the item you wish to update")
    display_catalog()
    id = input("Choose the id you want to edit: ")
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            print("Updating " + item.title)
            new_stock = input("Enter the new stock amount: ")
            print("The new stock of " + item.title + " is " + new_stock)
            item.stock = new_stock
    if(not found):
        print("Error, invalid ID. Try again.")


def cheapest_item():
    print_header("Cheapest Item")
    temp_list = []
    for item in catalog:
        temp_list.append(item.price)
        temp = sorted(temp_list)
    for item in catalog:
        if(item.price == temp[0]):
            print_item(item)

# def three_most_exp():
#     print_header("Three Most Expensive Items")
#     prices = []
#     for item in catalog:
#         prices.append(item.price)
#     prices.sort(reverse=True)

#     # print(prices[0])

#     # print(prices[1])

#     # print(prices[2])

#     for item in catalog:
#         if(item.price == prices[0] and item.price == prices[1] and item.price == prices[2]):
#             print_item(item)


# instructions
deserialize_catalog()

input("Press enter to continue...")

opc = ""
while(opc != "x"):
    clear()
    print_menu()

    opc = input("Please select an option: ")

    if(opc == "1"):
        registered_item()
        serialize_catalog()

    elif(opc == "2"):

        display_catalog()

    elif(opc == "3"):

        out_stock_item()

    elif(opc == "4"):

        stock_value()

    elif(opc == "5"):

        update_price()
        serialize_catalog()

    elif(opc == "6"):

        delete_item()
        serialize_catalog()

    elif(opc == "7"):

        update_stock()
        serialize_catalog()

    elif(opc == "8"):

        display_categories()

    elif(opc == "9"):

        cheapest_item()

    elif(opc == "10"):

        # three_most_exp()

        input("Press enter to continue...")
