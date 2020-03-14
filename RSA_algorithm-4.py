# 1 choosing 2 prime numbers
import random

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1,2):   # only odd numbers
        if n % i == 0:
            return False    
    return True

def reverse_prime(n):   #check for exponent
    fact_set = set()
    for i in range(2, n + 1):
        if (n % i == 0):
            n //= i
            fact_set.add(i)
    return fact_set

def rev_prime_check(prime_one, prime_two):
    badnum_set1 = reverse_prime(prime_one)
    badnum_set2 = reverse_prime(prime_two)
    if len(badnum_set1.union(badnum_set2)) == len(badnum_set2) + len(badnum_set1):
        return True
    else:
        return False

primes = [i for i in range(1,100) if isPrime(i)]
n_prime = random.choice(primes)
m_prime = random.choice(primes)

print('''
Первое простое число: ''' + str(n_prime) + '''
Второе простое число: ''' + str(m_prime) + '''
''')

modulus = n_prime * m_prime

eiler_function = (n_prime - 1) * (m_prime - 1)

open_exponent_vars = [i for i in primes if (i < eiler_function) and rev_prime_check(eiler_function,i)]
open_exponent = random.choice(open_exponent_vars)

public_key = [open_exponent, modulus]

print('Публичный ключ: ', public_key)

d_list = []
for i in range(1, 10000):
    if (i * open_exponent) % eiler_function == 1:
        d_list.append(i)

d_num = random.choice(d_list)
private_key = [d_num, modulus]

print('Закрытый ключ: ', private_key)
print('Введите сообщение-число меньше', modulus, ':')
message = int(input())

crypted = (message ** public_key[0]) % public_key[1]

print('Зашифрованное сообщение выглядит так: ', crypted)

encrypted = (crypted ** private_key[0]) % private_key[1]

print('Расшифрованное сообщение выглядит так: ', encrypted)
