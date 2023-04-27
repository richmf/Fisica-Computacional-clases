#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import *
from matplotlib import animation,rc
#from matplotlib import FuncAnimation # Algunas veces solo funciona con esto
#from IPython.display import HTML #Esto solo sirve para ver los videos en los notebooks


# In[2]:


t = linspace(0,4*pi)
x = cos(t)
y = sin(t)


# In[3]:


fig = figure()
ejes = axes( xlim=(-1.1,1.1) , ylim=(-1.1,1.1) )
circulo, = ejes.plot([],[],c='r')

def animar(i):
    circulo.set_data(x[:i],y[:i])
    return circulo,

pelicula = animation.FuncAnimation(fig,animar,frames=len(t),blit=True)
pelicula.save('mi_peli1.mp4')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




