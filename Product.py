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
    def current_stock_quantity(cls,estimated_monthly_production,sale_of_product):
        cls._stock_quantity =  cls._stock_quantity + estimated_monthly_production - sale_of_product
        return cls._stock_quantity
    
