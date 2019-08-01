'''program to print first n natural numbers divisible by 3 and 6 not by 9'''
n = int(input("Enter the value of n"))
i=1
c=0
while True:
    if (i % 3 == 0 and i % 6 == 0) and (not i % 9 == 0):
       c+=1
       print(i,end=" ")
    if (c == n):
        break
    i += 1    
