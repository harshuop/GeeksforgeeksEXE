def simple_interest(p,t,r):
    return (p*t*r)/100


input1 = int(input('Principal amount: '))
input2 = int(input('Time: '))
input3 = int(input('Rate of interest: '))

sol = simple_interest(input1,input2,input3)
print(f"\n{sol}")

