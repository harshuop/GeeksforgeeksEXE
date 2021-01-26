def compound_interest(p,r,t):
    a = p*(1+(r/100))**t
    return a-p
in1 = float(input('Principal: '))
in2 = float(input('Rate: '))
in3 = float(input('Time: '))

sol = compound_interest(in1, in2, in3)
print(sol)
    
