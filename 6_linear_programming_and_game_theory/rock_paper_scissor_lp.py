# Use simplex method to find Nash equilibrium of rock-paper-scissors
import numpy as np
from scipy.optimize import linprog 

#parameter vector x = (v,x1,x2,x3)
#minimize -v = (-1,0,0,0)*x
c = [-1,0,0,0]

#payout matrix A = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
#define inequality constraints
#of the form Mx <= b
M = [[1,0,-1,1],[1,1,0,-1],[1,-1,1,0]]
b = [0,0,0]

#define equality constraints
M_eq = [[0,1,1,1]]
b_eq = [1]

#define lower and upper bounds
v_bounds = (None,None)
x1_bounds = (0,None)
x2_bounds = (0,None)
x3_bounds = (0,None)

res = linprog(c, A_ub=M, b_ub=b, \
  A_eq=M_eq, b_eq=b_eq,  \
  bounds=(v_bounds, x1_bounds, x2_bounds, x3_bounds), \
  options={"disp": True})

print res
