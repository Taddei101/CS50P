import time
inicio = time.perf_counter()

primes = list()

for number in range (2,1000):
    c=0
    for i in range (1, number+1):
        if number % i == 0:
            c +=1
            if c > 2:
                break
    if c<=2:
        primes.append(number)
    

print(f"Prime numbers in range: {len(primes)}\n{primes}")


fim = time.perf_counter()
print(f"Tempo: {fim - inicio:.6f}s")


