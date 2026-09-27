import time
import sympy

inicio = time.perf_counter()

primes = list()

for number in range (2,1000):
    if sympy.isprime(number):
        primes.append(number)
    

print(f"Prime numbers in range: {len(primes)}\n{primes}")


fim = time.perf_counter()
print(f"Tempo: {fim - inicio:.6f}s")

