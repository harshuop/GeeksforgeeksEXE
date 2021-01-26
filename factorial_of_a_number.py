def fac(a):
    return 1 if (a==0 or a==1) else a * fac(a-1);
a = int(input('Your num: '))
print(fac(a))

