
"""
class Product:

"""














print("Welcome to Programming Principles Sample Product Inventory")

def run():
    while True:
        try:
            product_code = int(input("Please enter the Product Code: "))
            if 100 <= product_code <= 1000:
                print("You have entered {} as the Product Code".format(product_code))
                break
            else:
                print("Invalid Input for Product Code! Please Enter a number between 100-1000!")
                continue
        except ValueError:
            print("Invalid Input for Product Code! Please enter a valid Integer Type!")
            continue

    while True:
        try:
            product_name = str(input("Please enter the Product Name: "))
            print("You have entered {} as the Product name".format(product_name))
            break
        except ValueError:
            print("Invalid Input for Product Name! Please enter a string character!")
            continue


    while True:
        try: 
            product_sale_price = float(input("Please enter the Product Sale Price: "))
            if product_sale_price > 0:
                print("You have entered {} $CAD as the Product Sale price".format(product_sale_price))
                break
        except ValueError:
            print("Invalid Input for Product Sale Price! Please enter a number greater than 0!")
            continue


    while True:
        try: 
            product_manufacture_cost = float(input("Please enter the Product Manufacture Cost: "))
            if product_manufacture_cost > 0:
                print("You have entered {} $CAD as the Product Manufacture Cost".format(product_manufacture_cost))
                break
        except ValueError:
            print("Invalid Input for Product Manufacture Cost! Please enter a valid input!")
            continue


    while True:
        try:
            stock_level = int(input("Please enter the Current Stock Level: "))
            if stock_level > 0:
                print("You have entered {} in stock quantity".format(stock_level))
                break
        except ValueError:
            print("Invalid Input for Stock Level! Please enter a number above 0!")
            continue

    while True:
        try:
            estimated_monthly_units_manufactured = int(input("Please enter the Estimated Monthly Units Manufactured: "))
            if estimated_monthly_units_manufactured > 0:
                print("You have entered {} as the Estimated Montly Units Manufactured".format(estimated_monthly_units_manufactured))
                break
        except ValueError:
            print("Invalid Input for Estimated Monthly Units! Please enter a number above 0!")
            continue


run()