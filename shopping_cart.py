
# shopping_cart.py

import datetime

Tax_Rate = 0.06

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"

def divider():
    """
    Returns a divider for displaying purposes.

    Example: divider()

    Returns: -------------------
    """
    return "-------------------"

def find_product(product_id, all_products):
    """
    Looks up a product given its unique identifier from a provided list of products.

    Source: https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart.py

    Params: 
        my_price (int) like 8
        all_products (list)
    Example (given the prodcuts list in this file): to_usd(5, products)

    Returns: {'id': 5, 'name': 'Green Chile Anytime Sauce', 'department': 'pantry', 'aisle': 'marinades meat preparation', 'price': 7.99}
    """
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    return matching_product

def tax(rate, total):
    """
    Returns the tax amount given the tax rate and pretax total.

    Params: 
        rate (float) like 0.08 
        total(integer or float) like 150

    Example: to_usd(0.08,100)

    Returns: 8
    """
    taxes = rate * total
    return taxes

def calculate_total_price(total, taxes):
    """
    Returns the total amount to pay given taxes and pretax amount.

    Params: 
        total (int or float) like 120
        taxes (int or float) like 13.25

    Example: calculate_total_price(35, 4.99)

    Returns: 39.99
    """
    total_price = total + taxes
    return total_price
  
def subtotal(balance,selected_product):
    """
    Calculates the balance given the initial balance and the price of the selected group. The function is useful in a loop to keep track of the balance given selected products.
    
    Params:
        balance (int or float) like 0
        selected_product (int or float) like 3.49

    Example: to_usd(0, 5.99)

    Returns: 5.99
    """
    balance = balance + ((selected_product["price"]))
    return balance

if __name__ == "__main__":

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

    total_price = 0
    selected_ids =[]
    product_ids =[str(p["id"]) for p in products] #creating a list including all valid ids

    #Input Collection and Validation

    while True:
        
        product_id = input("Please input a product identifier or 'Done' if you are finished: ")
        product_id = product_id.lower().title()

        if product_id == "Done":
            break
        elif product_id in product_ids:
            selected_ids.append(product_id)
        else:
            print ("Invalid entry. Please try again.")


    #Presentation of Final Outcome

    now = datetime.datetime.now()
    print(divider())
    print("PIED PIPER GROCERY")
    print("WWW.PIED-PIPER.COM")
    print(divider())
    print("CHECKOUT AT:")
    print(now.strftime("%Y-%m-%d %I:%M %p")) #taken from https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
    print(divider())
    print("SELECTED PRODUCTS:")

    for product_id in selected_ids:
        matching_product  = find_product(product_id, products)
        totall = subtotal(total_price,matching_product)
        price = to_usd(matching_product["price"])
        print("..." + matching_product["name"] + " (" + price +")")

    taxes = tax(Tax_Rate, totall)
    total = calculate_total_price(taxes,totall)

    print(divider())
    print("SUBTOTAL: " + to_usd(totall))
    print("TAX: " + to_usd(taxes))
    print("TOTAL: " + to_usd(total))
    print(divider())
    print("THANKS, SEE YOU AGAIN SOON!")
    print(divider())
