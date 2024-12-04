"""

Python Program to find and display prime nos in a given number list
- Gayathri L
Loop and divide the number by upto half of the given number. if divisible
not a prime. Continue to next iteration
If undivided then a prime. Append to the list of prime numbers. Continue.
Display the list of Prime numbers at the end of the program
"""


lst=[10,501,22,37,100,999,87,351]
primelst=[]
for num in lst:
    notaprime=0
    for i in range(2,(num//2)+1):
        if num % i == 0:
            notaprime=1
    if notaprime == 0:
        primelst.append(num)
if len(primelst):
    print("Prime Numbers ->", primelst)
else:
    print("No Numbers are prime in the list:", lst)
