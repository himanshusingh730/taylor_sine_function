from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
def fact(n):
	out=1
	for i in range(1,n+1):
		out=out*i
	return out
def secout(n):
	if(n%2 == 0):
		return 1
	else:
		return -1
def exp(x,n):
	out=1;
	for i in range(1,n+1):
		out=out*x
	return out
def ternfm(x,n):
	out= (exp(x,2*n+1)*secout(n))/fact(2*n+1)
	return out
def sinne(x,a):
	out=0;
	for i in range(0,a):
		out = out+ternfm(x,i)
	return out
x=np.arange(-30,30,0.01)
def setyarr(num):
	a=[]
	for i in np.arange(-30,30,0.01):
		a.append(sinne(i,num))
	y = np.array(a)
	return y
for num in range(1,30):
	y= setyarr(num)
	plt.plot(x,y)
	axes = plt.gca()
	axes.set_ylim([-2,2])
	plt.show()
	plt.pause(1)
	plt.close()		
