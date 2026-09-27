import numpy as np
import matplotlib.pyplot as plt

y2 = 0.015
y1 = 0.005
g = 9.81
L = 0.065

F1 = np.sqrt(1/2*y2/y1*(y2/y1+1))

v1 = F1*np.sqrt(g*y1)

S1 = L*y1

Q = v1*S1

q = Q/L

F2 = q/np.sqrt(g*y2**3)


print("Fr1 = ", F1)

print("Q = ", Q)

print("Fr2 = ", F2)

##print("H*1 = ", H_1)
##
##print("y1 = ", y1)


