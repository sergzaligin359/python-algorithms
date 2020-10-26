a = int(input('input first num: '))
b = int(input('input second num: '))
c = int(input('input third num: '))

m = a

if m < b:
    m = b
if m < c:
    m = c
print(f'Max num is: {m}')