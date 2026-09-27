import time
inicio = time.perf_counter()

primes = list()

for number in range (2,1000):
    is_prime = True
    for i in range (2, int(number**(0.5)+1)):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    

print(f"Prime numbers in range: {len(primes)}\n{primes}")


fim = time.perf_counter()
print(f"Tempo: {fim - inicio:.6f}s")


