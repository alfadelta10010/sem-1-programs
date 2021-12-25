# 1) Using functions generate prime numbers using method of Sieve of Eratosthenes
def Sieve_eratosthenes(n):
    prime_nums = []
    for i in range(2, n + 1):
        if i not in prime_nums:
            print(i)
            for j in range(i * i, n + 1, i):
                prime_nums.append(j)


num = int(input("Generate primes till?: "))
Sieve_eratosthenes(num)
