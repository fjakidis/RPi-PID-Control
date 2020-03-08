from sympy import *

l1 = 40
l2 = 40
k = Symbol('k',real = True)
t = Symbol('t',real = True)
x = 60
y = 20
#conds = [(-pi<t),(t<pi),(k<pi),(-pi<k)]
e1 = l1*sin(t)+l2*sin(k)-y
e2 = l1*cos(t)+l2*cos(k)-x
eqns = [e1,e2]
var = [t,k]
#gensol = diophantine(eqns, v, var)
gensol = solve(eqns,var)


pprint(float(gensol[1][0]))

