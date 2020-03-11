#from sympy import *
import sympy as sp
from sympy.plotting import plot3d

# Symbols
a = sp.Symbol('a')
b = sp.Symbol('b')

k = sp.Symbol('k')
t = sp.Symbol('t')

x = sp.Symbol('x')
y = sp.Symbol('y')

#conds = [(-pi<t),(t<pi),(k<pi),(-pi<k)]
e1 = a*sp.sin(t)+b*sp.sin(k)
e2 = a*sp.cos(t)+b*sp.cos(k)

E1 = sp.Eq(x,e1)
E2 = sp.Eq(y,e2)

eqns = [E1,E2]
var = [t,k]

#gensol = sp.nonlinsolve(eqns,var)





