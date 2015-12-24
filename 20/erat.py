
# coding: utf-8

# In[1]:

from functools import reduce


# In[2]:

_d = {}
_startat = 2
_primes = []


# In[3]:

def primes(n=None):
    if n and not isinstance(n, int): raise TypeError(repr(n) + " is not int")
    global _d, _startat, _primes
    for q in _primes:
        if n and q > n: break
        yield q
    if not n or n >= _startat:
        q = _startat
        while True:
            if not q in _d:
                _primes.append(q)
                if not n and _startat <= q: _startat = q + 1
                yield q
                _d[q * q] = [q]
            else:
                for p in _d[q]: _d.setdefault(p + q, []).append(p)
                del _d[q]
            q += 1
            if n and q > n:
                _startat = q
                return


# In[4]:

def primefactors(n):
    if n == 0: raise ZeroDivisionError
    if not isinstance(n, int): raise TypeError(repr(n) + " is not int")
    if n < 0:
        n = -n
        pairs = [(-1, 1)]
    else:
        pairs = []
    for prime in primes():
        e = 0
        value, mod = divmod(n, prime)
        while mod == 0:
            n = value
            e += 1
            value, mod = divmod(n, prime)
        if not e == 0: pairs.append((prime, e))
        if value <= prime: break
    if n > 1: pairs.append((n, 1))
    return pairs


# In[5]:

def divisorGen(n):
    if not isinstance(n, int): raise TypeError(repr(n) + " is not int")
    factors = primefactors(n)
    nfactors = len(factors)
    f = [0] * nfactors
    divisors = []
    while True:
        divisors.append(reduce(lambda x, y: x * factors[y][0]**f[y], range(nfactors), 1))
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]: break
            f[i] = 0
            i += 1
            if i >= nfactors: return divisors

