n = int(input("Enter number of person:"))
dist = int(input("Enter the distance in km:"))
milage = int(input("Enter the milage in km:"))
fuel_price=int(input("Enter the fuel price"))

no_liters=dist / milage
total_cost=no_liters * fuel_price
price_per_head = total_cost / n
print(f"Total cost per person is {price_per_head}")
