n = int(input())
hs = [ int(_) for _ in input().split()]
#
# #
#
k = 1800010
# k = 100
sieve = {0: False, 1 : False, 2 : True}

for i in range(3, k):
    sieve[i] = True

p = 2
while p < k:
    if sieve[p]:
        i = 2*p
        while i < k:
            sieve[i] = False
            i += p
    p += 1

def is_prime(i):
    return sieve[i]

# for i in range(k):
#     if sieve[i]:
#         print(i)


def kp(i, c_s, primes):
    # print(i, c_s, primes)

    if i == n:
        return

    if i > 0:
        if is_prime(hs[i]):
            # print(i, hs[i])
            primes[hs[i]] = True

        if is_prime(c_s):
            # print(i, c_s)
            primes[c_s] = True

    for p in range(i + 1, n):
        kp(p, c_s + hs[i], primes)



primes = {}
for i in range(n):
    kp(i-1, 0, primes)

print(len(primes))
