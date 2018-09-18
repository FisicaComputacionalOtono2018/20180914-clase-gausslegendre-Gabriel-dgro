#Autor: Gabriel Reyes
#Gauss


from sympy import *
x=symbols('x')

def fac(n):
	M=1
	F=1
	while M<float(n):
		M=M+1
		F=F*M
	return (F)

n=input("Grado del pólinomio: ")
r=input("Dame x: ")

funcion=(x**2-1)**float(n)

derivada=diff(funcion,x,n)
evaluacion=derivada.subs(x, float(r))


polinomio=(1/2**float(n)*fac(n))*(derivada)

derivadab=diff(polinomio,x,1)

print(derivadab)
 

