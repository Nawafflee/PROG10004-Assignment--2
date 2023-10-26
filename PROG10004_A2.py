import random

"""
Github Repository https://github.com/Nawafflee/PROG10004-Assignment--2
"""

# Defined a class called Product in order to simulate the Product's inventory
class Product:

    #Constructor to Initialize Product instance with estimated monthly production 
    def __init__(self,estimated_monthly_production):
        self._estimated_monthly_production = estimated_monthly_production

    """
    The sale_of_product method calculates and returns the number of units sold for a 
    given month based on a random value within a range defined by self._negative_range_of_units_manufactured 
    and _positive_range_of_units_manufactured.
    """

    def sale_of_product(self,estimated_monthly_production):
        self._negative_range_of_units_manufactured = estimated_monthly_production - 10
        self._positive_range_of_units_manufactured = estimated_monthly_production + 10
        self.sale_of_product = random.randint(self._negative_range_of_units_manufactured,self._positive_range_of_units_manufactured)
        return self.sale_of_product
    
    """
    Class method that sets the class variable stock_quantity to a specified value, 
    allowing you to change the stock_quantity for the current month.
    """
    
    @classmethod
    def change_in_stock(cls,stock_quantity):
        cls._stock_quantity = stock_quantity

    """
    A class method that calculates the stock quantity based on the monthly production and units sold.
    It updates the class variable stock_quantity.
    """
    
    @classmethod
    def current_stock_quantity(cls,monthly_production,sale_of_product):
        cls._stock_quantity =  cls._stock_quantity + monthly_production - sale_of_product
        return cls._stock_quantity
    




def run():
    print("Welcome to Programming Principles Sample Product Inventory")

    """
    In the cases below we use a while loop to execute the conditions as long as they are True
    We use Try and except as statements for exception handling try occurs when an exception may occur while except 
    determines how our program should handle these exceptions we use ValueError when we enter something 
    that cannot be converted to an integer which displays an error message
    """

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
        
        #Used for Sanity check even though a number can be included as part of a string kept due for good coding practices
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


    print("\n******* Welcome to Programming Principles Sample Product Inventory *******")
    print("Product Code {}: ".format(product_code))
    print("Product Name {}: ".format(product_name))
    print("\n---------------------------------------------------------------------------")
    print("\nSale Price {} CAD: ".format(product_sale_price))
    print("Manufacture Cost {} CAD: ".format(product_manufacture_cost))
    print("Monthly Production {} units (Approx.)".format(estimated_monthly_units_manufactured))


run()