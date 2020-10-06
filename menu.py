import os
import time


def print_menu():
    print("-"*30)
    print(" Warehouse control")
    print("-"*30)

    print("[1] Register new item")
    print("[2] Display catalog")
    print("[3] Display items out of stock")
    print("[4] Stock Value")
    print("[5] Update item price")
    print("[6] Delete an item")  # similar to option 5
    print("[x] Close")


def clear():

    # for windows
    # os.system('cls')
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

    # Ubuntu version 10.10
    # os.system("clear")


def print_item(item):
    print(str(item.id).ljust(5) + " | " + item.title.ljust(20) + " | " + item.category.ljust(15) +
          " | " + str(item.stock).ljust(5) + " | " + str(item.price).ljust(10))


def print_header(title):
    clear()
    print("-" * 50)
    print(title)
    print("-" * 50)
