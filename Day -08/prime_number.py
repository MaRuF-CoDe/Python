n = int(input("Check this number: "))

def prime_checker(number):
    for i in range(2,number):
        if number % i == 0 :
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")
prime_checker(number=n)