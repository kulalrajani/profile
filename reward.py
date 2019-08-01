reward = int(input("Enter your reward points:"))
if reward >= 0 and reward <=1000:
    ctype = "SILVER"
elif reward > 1000 and reward <=10000: 
    ctype = "GOLD"
else:
    ctype = "PLATINUM"

print(f"Welcome {ctype} card holder")    
