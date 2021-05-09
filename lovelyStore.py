# This is a project of a small-business ownership and open up a furniture store called Lovely Loveseats

# A nice ASCII Art for the initialize the terminal.
wellcome ="""

      __        ___                   __        ___  __   ___      ___  __  
|    /  \ \  / |__  |    \ /    |    /  \ \  / |__  /__` |__   /\   |  /__` 
|___ \__/  \/  |___ |___  |     |___ \__/  \/  |___ .__/ |___ /~~\  |  .__/ 
                                                                            
"""

# Store Databese of Products and prices.
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_sette_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

# The var for the 8.8% sales tax
sales_tax = .088

# Our First Customer
customer_one_total = 0
customer_one_itemization = ""

# Customer cart
customer_one_total += lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization += lovely_loveseat_description + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)