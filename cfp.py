def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_two_digit_primes():
    """
    Prints all 2-digit prime numbers.
    """
    for num in range(10, 100):
        if is_prime(num):
            print(num) 

print_two_digit_primes()