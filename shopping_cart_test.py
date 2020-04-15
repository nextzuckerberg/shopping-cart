import pytest # for pytest.raises (see: https://docs.pytest.org/en/latest/assert.html)

from shopping_cart import to_usd, Tax_Rate, find_product, tax, calculate_total_price, subtotal, divider

def test_tax_rate():
    assert(Tax_Rate) == 0.06

def test_to_usd():
    #adapted from https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_find_product():
    #adapted from https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    # if there is no match, it should raise an IndexError
    with pytest.raises(IndexError):
        find_product("2222", products)

def test_tax():
    # it should return the the product of two numbers
    assert tax(0.05,100) == 5

def test_calculate_total_price():
    # it should return the sum of two numbers
    assert calculate_total_price (3.21, 10) == 13.21

def test_subtotal():
    # it should return the sum of two numbers
    selected_product =  {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49}
    assert subtotal (0, selected_product) == 2.49

def test_divider():
    #it should return the divider/line
    assert divider() == "-------------------"
