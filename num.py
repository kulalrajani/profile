num = int(input("Enter the number:"))
temp = num
sum = 0
while not num == 0:
    r = num % 10
    sum = sum + r ** 3
    num = num // 10
if sum == temp:
    print(f"{temp} is a armstrong number")
else:
     print(f"{temp} is not a armstrong number")       