def Akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Akk(m - 1, 1)
    else:
        return Akk(m - 1, Akk(m , n - 1))

print(Akk(3, 4))
