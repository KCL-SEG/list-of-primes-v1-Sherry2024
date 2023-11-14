"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    prime_list = []
    num = 2 
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

