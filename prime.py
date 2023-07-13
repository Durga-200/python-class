#Write a program to checking if the number is prime or not using function.
def is_prime(number):
    d=0
    for i in range(1,number+1,1):
        if number%i==0:
            d+=1
    if d<=2:
        return True
    else:
        return False
number =int(input("enter input:"))   
if is_prime(number)==True:
    print(f"{number}is prime")
else:
    print(f"{number} is composite")
