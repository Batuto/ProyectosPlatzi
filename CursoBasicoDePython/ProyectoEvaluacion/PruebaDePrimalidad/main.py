import math


MSG = """This program compute if a number
is prime or not, following the
AKS pimality test.
"""


def generator(n):
    # Following the AKS algorithm make a generator
    # for the polinomial expansion. source: rosettacode.org
    c = 1
    for i in range(n//2+1):
        c = c*(n-i)//(i+1)
        yield c


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for x in generator(number):
        if x % number:
        # Return early, we don't want to compute all possible solutions.
            return False
    return True


def main():
    print(MSG)
    number = int(input("Write a number: "))
    print("It is prime" if is_prime(number) else "It is not prime")


if __name__ == '__main__':
	main()
