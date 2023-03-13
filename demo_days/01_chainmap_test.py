#!/usr/local/bin/python3
from collections import ChainMap

location_info = {"shop_no": "1", "street": "London Road"}
menu_info = {"coffee_1": "espresso", "coffee_3": "Latte", "coffee_2": "Flat White"}
shop_dim_info = {"length": "200m", "width": "200m"}
coffee_shop_data = ChainMap(location_info, menu_info, shop_dim_info)
print(coffee_shop_data["coffee_1"])
coffee_shop_data["coffee_1"] = "Mocha"
print(coffee_shop_data["coffee_1"])
print(coffee_shop_data["length"])
print(coffee_shop_data["coffee_3"])
print(coffee_shop_data["street"])
