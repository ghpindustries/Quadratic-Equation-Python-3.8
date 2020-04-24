#Quadratic equation
a=int(input())
b=int(input())
c=int(input())

d_d=b**2-(4*a*c)
d=d_d**(1/2)
sol1 = ((-b)+d)/(2*a)
sol2 = ((-b)-d)/(2*a)

#Check if solution exists

if d_d < 0:
   print('Solution exists in complex numbers')
else:
   print('x = {0} or x = {1}'.format(sol1,sol2))
