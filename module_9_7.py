def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        prime = True
        if result > 1:
            for i in range(2, result // 2):
                if result % i == 0:
                    prime = False
                    break
            if prime:
                print('Простое')
            else:
                print('Составное')
        return result
    return wrapper

@ is_prime
def sum_three(a, b ,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)


@is_prime
def sum_prod(a, b, c, d):
    return a * b + c * d

print(sum_prod(3, 1, 5, 8))
print(sum_prod(3, 6, 5, 4))