def prime_num(start, end, value):
    prime = []
    n_prime = []
    for i in range(start, end+1):
        if i > 1:
            for a in range(2,i):
                if i%a == 0:
                    n_prime.append(i)
                    break
            else:
                prime.append(i)
    if value.lower() == 'p':
        print(f"Primes: {prime}")
    else:
        print(f"Non-Primes: {n_prime}")

s = int(input('Upper Limit: '))
e = int(input('Lower Limit: '))
v = input('(Prime:"np" / Non-Prime:"p"): ')

prime_num(s,e,v)

