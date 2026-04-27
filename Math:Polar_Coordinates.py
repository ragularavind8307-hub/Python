import cmath
x=complex(input())
a=x.real
b=x.imag
print(abs(complex(a,b)))
print(cmath.phase(complex(a,b)))
