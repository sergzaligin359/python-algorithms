def gcd(m, n):
    if m == n:
        return m
    while(m != n):
        if(m > n):
            m = m - n
        if(n > m):
            n = n - m
    return m

print(gcd(56, 24))
