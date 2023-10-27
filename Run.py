import Product


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
            product_code = int(input("Please enter the Product Code between (100-1000): "))
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

    #Month 1
    
    #Creates an Object instance of the Product Class for Month_1 and initialize it with estimated_monthly_units_manufactured
    Month_1 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 1
    print("\nMonth 1: ")

    # Print the Manufactured Units for for Month 1.
    print("\tManufactured : {} Units".format(Month_1._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 1.
    print("\tSold: {} Units".format(Month_1.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 1st month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 1.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product))

    #print("Change in Stock ",Month_1.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_1.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product))

    # Print the updated stock level for month 1.
    print("\tStock : {} Units".format(Month_1._stock_quantity))


    #Month 2

    #Creates an Object instance of the Product Class for Month_2 and initialize it with estimated_monthly_units_manufactured
    Month_2 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 2
    print("\nMonth 2: ")

    # Print the Manufactured Units for for Month 2.
    print("\tManufactured : {} Units".format(Month_2._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 2.
    print("\tSold: {} Units".format(Month_2.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 2nd month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 1.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product))

    #print("Change in Stock ",Month_2.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_2.current_stock_quantity(estimated_monthly_units_manufactured,Month_1.sale_of_product))

    # Print the updated stock level for month 2.
    print("\tStock : {} Units".format(Month_2._stock_quantity))


    #Month 3 

    #Creates an Object instance of the Product Class for Month_3 and initialize it with estimated_monthly_units_manufactured
    Month_3 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 3
    print("\nMonth 3: ")

    # Print the Manufactured Units for for Month 3.
    print("\tManufactured : {} Units".format(Month_3._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 3.
    print("\tSold: {} Units".format(Month_3.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 3rd month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 2.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_2.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_2.sale_of_product))

    #print("Change in Stock ",Month_3.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_3.current_stock_quantity(estimated_monthly_units_manufactured,Month_2.sale_of_product))

    # Print the updated stock level for month 3.
    print("\tStock : {} Units".format(Month_3._stock_quantity))


    #Month 4

    #Creates an Object instance of the Product Class for Month_4 and initialize it with estimated_monthly_units_manufactured
    Month_4 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 4
    print("\nMonth 4: ")

    # Print the Manufactured Units for for Month 4
    print("\tManufactured : {} Units".format(Month_4._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 4.
    print("\tSold: {} Units".format(Month_4.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 4th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 3.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_3.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_3.sale_of_product))

    #print("Change in Stock ",Month_4.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_4.current_stock_quantity(estimated_monthly_units_manufactured,Month_3.sale_of_product))

    # Print the updated stock level for month 4.
    print("\tStock : {} Units".format(Month_4._stock_quantity))


    #Month 5

    #Creates an Object instance of the Product Class for Month_5 and initialize it with estimated_monthly_units_manufactured
    Month_5 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 5
    print("\nMonth 5: ")

    # Print the Manufactured Units for for Month 5
    print("\tManufactured : {} Units".format(Month_5._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 5.
    print("\tSold: {} Units".format(Month_5.sale_of_product(estimated_monthly_units_manufactured)))
    
    # Change the stock amount based on the stock level of the 5th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 4.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_4.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_4.sale_of_product))

    #print("Change in Stock ",Month_5.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_5.current_stock_quantity(estimated_monthly_units_manufactured,Month_4.sale_of_product))

    # Print the updated stock level for month 5.
    print("\tStock : {} Units".format(Month_5._stock_quantity))


    #Month 6

    #Creates an Object instance of the Product Class for Month_6 and initialize it with estimated_monthly_units_manufactured
    Month_6 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 6
    print("\nMonth 6: ")

    # Print the Manufactured Units for for Month 6
    print("\tManufactured : {} Units".format(Month_6._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 6
    print("\tSold: {} Units".format(Month_6.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 6th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 5.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_5.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_5.sale_of_product))

    #print("Change in Stock ",Month_6.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_6.current_stock_quantity(estimated_monthly_units_manufactured,Month_5.sale_of_product))

    # Print the updated stock level for month 6.
    print("\tStock : {} Units".format(Month_6._stock_quantity))

    #Month 7

    #Creates an Object instance of the Product Class for Month_7 and initialize it with estimated_monthly_units_manufactured
    Month_7 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 7
    print("\nMonth 7: ")

    # Print the Manufactured Units for for Month 7
    print("\tManufactured : {} Units".format(Month_7._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 7
    print("\tSold: {} Units".format(Month_7.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 7th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 6.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_6.sale_of_product)


    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_6.sale_of_product))

    #print("Change in Stock ",Month_7.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_7.current_stock_quantity(estimated_monthly_units_manufactured,Month_6.sale_of_product))

    # Print the updated stock level for month 7.
    print("\tStock : {} Units".format(Month_7._stock_quantity))

    #Month 8
    #Creates an Object instance of the Product Class for Month_8 and initialize it with estimated_monthly_units_manufactured
    Month_8 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 8
    print("\nMonth 8: ")

    # Print the Manufactured Units for for Month 8
    print("\tManufactured : {} Units".format(Month_8._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 8
    print("\tSold: {} Units".format(Month_8.sale_of_product(estimated_monthly_units_manufactured)))


    # Change the stock amount based on the stock level of the 8th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 7.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_7.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_7.sale_of_product))

    #print("Change in Stock ",Month_8.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_8.current_stock_quantity(estimated_monthly_units_manufactured,Month_7.sale_of_product))

    # Print the updated stock level for month 8.
    print("\tStock : {} Units".format(Month_8._stock_quantity))

    #Month 9

    #Creates an Object instance of the Product Class for Month_9 and initialize it with estimated_monthly_units_manufactured
    Month_9 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 9
    print("\nMonth 9: ")

    # Print the Manufactured Units for for Month 9
    print("\tManufactured : {} Units".format(Month_9._estimated_monthly_production)) #Calls the Attribute


    # Calculate and print the number of units sold for Month 9
    print("\tSold: {} Units".format(Month_9.sale_of_product(estimated_monthly_units_manufactured)))


    # Change the stock amount based on the stock level of the 9th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 8.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_8.sale_of_product)


    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_8.sale_of_product))

    #print("Change in Stock ",Month_9.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_9.current_stock_quantity(estimated_monthly_units_manufactured,Month_8.sale_of_product))

    # Print the updated stock level for month 9.
    print("\tStock : {} Units".format(Month_9._stock_quantity))


    #Month 10

    #Creates an Object instance of the Product Class for Month_10 and initialize it with estimated_monthly_units_manufactured
    Month_10 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 10
    print("\nMonth 10: ")

    # Print the Manufactured Units for for Month 10
    print("\tManufactured : {} Units".format(Month_10._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 10
    print("\tSold: {} Units".format(Month_10.sale_of_product(estimated_monthly_units_manufactured)))



    # Change the stock amount based on the stock level of the 10th month.
    Product.Product.change_in_stock(stock_level)



    # Calculate and update the stock quantity based on monthly production and units sold for month 9.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_9.sale_of_product)


    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_9.sale_of_product))

    #print("Change in Stock ",Month_10.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_10.current_stock_quantity(estimated_monthly_units_manufactured,Month_9.sale_of_product))

    # Print the updated stock level for month 10.
    print("\tStock : {} Units".format(Month_10._stock_quantity))



    #Month 11
    #Creates an Object instance of the Product Class for Month_11 and initialize it with estimated_monthly_units_manufactured
    Month_11 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 11
    print("\nMonth 11: ")


    # Print the Manufactured Units for for Month 11
    print("\tManufactured : {} Units".format(Month_11._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 11
    print("\tSold: {} Units".format(Month_11.sale_of_product(estimated_monthly_units_manufactured)))



    # Change the stock amount based on the stock level of the 11th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 10.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_10.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_10.sale_of_product))

    #print("Change in Stock ",Month_11.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_11.current_stock_quantity(estimated_monthly_units_manufactured,Month_10.sale_of_product))

    # Print the updated stock level for month 11.
    print("\tStock : {} Units".format(Month_11._stock_quantity))


    #Month 12

    #Creates an Object instance of the Product Class for Month_12 and initialize it with estimated_monthly_units_manufactured
    Month_12 = Product.Product(estimated_monthly_units_manufactured)

    # Print Month 12
    print("\nMonth 12: ")

    # Print the Manufactured Units for for Month 12
    print("\tManufactured : {} Units".format(Month_12._estimated_monthly_production)) #Calls the Attribute

    # Calculate and print the number of units sold for Month 12
    print("\tSold: {} Units".format(Month_12.sale_of_product(estimated_monthly_units_manufactured)))

    # Change the stock amount based on the stock level of the 12th month.
    Product.Product.change_in_stock(stock_level)

    # Calculate and update the stock quantity based on monthly production and units sold for month 11.
    Product.Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_11.sale_of_product)

    #print("Change in stock ", Product.change_in_stock(stock_level))
    #print("Current Stock Quantity",Product.current_stock_quantity(estimated_monthly_units_manufactured,Month_11.sale_of_product))

    #print("Change in Stock ",Month_12.change_in_stock(stock_level))
    #print("Current Stock Quantity",Month_12.current_stock_quantity(estimated_monthly_units_manufactured,Month_11.sale_of_product))

    # Print the updated stock level for month 12.
    print("\tStock : {} Units".format(Month_12._stock_quantity))

    #Total Sold
    total_sold = Month_1.sale_of_product + Month_2.sale_of_product + Month_3.sale_of_product + Month_4.sale_of_product + Month_5.sale_of_product + Month_6.sale_of_product + Month_7.sale_of_product + Month_8.sale_of_product + Month_9.sale_of_product + Month_10.sale_of_product + Month_11.sale_of_product + Month_12.sale_of_product
    
    #Total Yearly Units Manufactured
    total_yearly_units_manufactured = estimated_monthly_units_manufactured * 12

    #Net Profit Formula
    net_profit = (total_sold * product_sale_price) - (total_yearly_units_manufactured * product_manufacture_cost)

    #Print Netprofit round precision to 2
    print("\nNet Profit/Loss ${} CAD".format(round(net_profit,2)))
    print("\n---End of Statement---")

    """
    #Object Types
    print("\nproduct_code ",type(product_code))
    print("product_name ",type(product_name))
    print("product_sale_price ",type(product_sale_price))
    print("product_manufacture_cost ",type(product_manufacture_cost))
    print("stock_level ",type(stock_level))
    print("estimated_monthly_units_manufactured ",type(estimated_monthly_units_manufactured))

    print("Month_1 ",type(Month_1))
    print("Month_2 ",type(Month_2))
    print("Month_3 ",type(Month_3))
    print("Month_4 ",type(Month_4))
    print("Month_5 ",type(Month_5))
    print("Month_6 ",type(Month_6))
    print("Month_7 ",type(Month_7))
    print("Month_8 ",type(Month_8))
    print("Month_9 ",type(Month_9))
    print("Month_10 ",type(Month_10))
    print("Month_11 ",type(Month_11))
    print("Month_12 ",type(Month_12))

    print("total_sold ",type(total_sold))
    print("total_yearly_units_manufactured ",type(total_yearly_units_manufactured))
    print("net_profit ",type(net_profit))
    """

#Run The Application
run()