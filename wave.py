import numpy as np
import matplotlib.pyplot as plt

#griddding
k = 50 #number of steps per 1 second
n = 34 #number of space steps

time = 10 #sec

dx = 1/n  #length of one space step
dt = 1/k  #length of one time step
c = 1     #speed of light
s = c*dt/dx #Courant number
total_time_steps = int(time/dt) #time
print("Courant number:",s)

x = np.linspace(0,1, n+1)

#initial condition
u0 = np.zeros(n+1)  #time-2
u = np.zeros(n+1)   #time-1
u1 = np.zeros(n+1)  #time
u0 = np.sin(2*np.pi*x) #u(x,0)= f(x)
u[0] = 0
u[n] = 0
ut = np.sin(2*np.pi*x) #du/dt = g(x)


#solving

#specific solution for the first time step
for i in range(1, n):
    u[i] = u0[i]-dt*ut[i]+0.5*s**2*(u0[i+1]-2*u0[i]+u0[i-1])
#solution for the next time steps
for t in range (2, total_time_steps+1):
    for i in range(1,n):
        u1[i] = 2 * u[i] - u0[i] + s**2*(u[i+1]-2*u[i]+u[i-1])

    #ploting
    plt.plot(x, u)
    plt.ylim([-1.2,1.2])
    plt.pause(0.00001)
    plt.clf()

    #cycle switching time variable
    u0 = np.copy(u) #time-2 = time-1
    u = np.copy(u1) #time-1 = time