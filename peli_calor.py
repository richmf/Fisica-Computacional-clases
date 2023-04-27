#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pylab import *
from matplotlib import animation,rc

def Mat_A_inv(Nx,r):
    A = zeros((Nx,Nx))
    dd , m_r = 2*(1+r) , -r
    for i in range(Nx-1):
        A[i,i] = dd
        A[i+1,i] = m_r
        A[i,i+1] = m_r
    A[-1,-1] = dd
    A_inv = inv(A)
    return A_inv

def Mat_B(Nx,r):
    B = zeros((Nx,Nx))
    dd = 2*(1-r)
    for i in range(Nx-1):
        B[i,i] = dd
        B[i+1,i] = r
        B[i,i+1] = r
    B[-1,-1] = dd
    return B

def Crank_Nicolson(Psi0,x,t,D=1):
    dt , dx = t[1]-t[0] , x[1]-x[0]
    Psi_total = zeros((len(t),len(Psi0)))
    Psi_total[0,:] = Psi0 
    r = D*dt/(dx**2)
    if r < 1:
        print('Voy a evolucionar con valor r= %2.2f' %r)
        Nx = len(Psi0[1:-1])
        Ainv , B = Mat_A_inv(Nx,r) , Mat_B(Nx,r)
        Ainv_B = dot(Ainv,B)
        for i in range(len(t)-1):
            Psi_total[i+1,1:-1] = dot(Ainv_B,Psi_total[i,1:-1])
    else:
        print('Valor de r= %2.2f no convergente' %r)
    return Psi_total

x = linspace(0,1,30)
t = linspace(0,0.4,500)
Psi0 = -x*(x-1)*sin(x)
Psi_total = Crank_Nicolson(Psi0,x,t)


fig = figure()
ejes = axes( xlim=(0,1) , ylim=(0,0.15) )
psi_frame, = ejes.plot([],[],c='tab:purple')

def animar(i):
    psi_frame.set_data(x,Psi_total[i,:])
    return psi_frame,

pelicula = animation.FuncAnimation(fig,animar,frames=len(t),blit=True)
pelicula.save('calor1.mp4')


# In[ ]:




