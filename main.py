numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime = 0
    for s in range(1, i+1):
        if i % s == 0:
            is_prime += 1
    if is_prime == 2:
        primes.append(i)
    else:
        is_prime = 0
        not_primes.append(i)
print("Primes:", primes)
print("Not primes:", not_primes)



