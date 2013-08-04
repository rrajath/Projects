# Prime Factorization - Have the user enter a number
# and find all Prime Factors (if there are any) and
# display them.

import math

def is_a_prime(x):
    if i % 2 == 0:
	return True
# No need to check if x is divisible by even numbers
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

# standard boilerplate
if __name__ == '__main__':
    n = int(raw_input('Enter the number to find prime factors of: '))

    factors = []

    for i in range(2, n + 1):
        while n % i == 0: # Thanks @madsulrik
            if is_a_prime(i):
                factors.append(i)
                n /= i
	if n == 1:
	    break
    print list(set(factors))
