""" Program to find grade of a student """
sub1 = int(input("Enter subject 1 marks:"))
sub2 = int(input("Enter subject 2 marks:"))
sub3 = int(input("Enter subject 3 marks:"))
if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    avg = (sub1 + sub2 + sub3) / 3
    if avg >= 35 and avg <= 65:
        print(f"Average is {avg} and Your grade is:C")
    elif avg > 65 and avg <= 85:
        print(f"Average is {avg} Your grade is:B")
    elif avg >85 and avg <= 100:
         print(f"Average is {avg} our grade is:A")
    else:
        print("Something really went wrong")     
else:
    print("Sorry!Better luck next time")         
