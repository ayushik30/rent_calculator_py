rent = int(input("enter the flat rent:"))
grocery_bill = int(input("enter the groceries ordered: "))
food_bill = int(input("enter the food ordered: "))
electricity_bill = int(input("enter the electricity spent:"))
charge_per_unit = int(input("charge per unit:"))
people = int(input("total number of prsons living:"))
total_bill = electricity_bill*charge_per_unit

output = (rent+grocery_bill+total_bill+food_bill)/people
print("total amount per head =", output)
