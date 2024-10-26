# A sample list. This code finds primes and ot prime natural numbers in and works for any lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes, not_primes = [], []             # Create empty lists for output
for i in range(len(numbers)):
    if (type(numbers[i]) != int or      # Check if the list element contain wrong type of data (not integer)
             numbers[i] <= 1):          # Check if the integer is negative, 0 or 1
        continue                        # Nothing to do further with such list item
    is_prime = True                     # Default prime flag
    for j in range(2, numbers[i]):      # Enumerate all numbers between 2 and the number being checked - 1
        if numbers[i] % j == 0:         # Check for divisibility of the list item by j
            is_prime = False            # Not prime flag if the number is divisible by j
            break                       # No need to check for other dividers when one has been already found
    if is_prime:
        primes.append(numbers[i])       # Adds only numbers with True is in is_prime flag
    else:
        not_primes.append(numbers[i])   # Adds only numbers with False is in is_prime flag
print("Primes:", primes)
print("Not primes:", not_primes)
