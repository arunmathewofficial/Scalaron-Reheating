import matplotlib.pyplot as plt
import numpy as np
import math 


alpha = 16.5 
Gamma = 1/(2.435*pow(10,5))
H_e = 1/(6.0*math.sqrt(alpha))

B = pow(pow(10, -29)/(264*2.435*15.1), 1/3)

tspan_1 = np.linspace(0,100000,num=100)
tspan_2 = np.linspace(100000,600000,num=100)

rho2 = []
for i in range(100):
    rho2.append( (3/11)*Gamma*tspan_2[i]*math.exp( -12.0*B*pow(tspan_2[i],5/3) )*( 1.0 + 33*B*pow(tspan_2[i],5/3)/20 )  )
    


# the function, which is y = x^3 here
rho = (3/11)*Gamma*tspan_1
#rho2 = (3/11)*Gamma*t*math.exp( -12.0*B*t )
#*( 1.0 + 33*B*pow(t,5/3)/20 )

 
 
 

fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=100)
#plt.axhline(y=0.9649, xmin=0, xmax=1, color='k', linestyle='dotted', linewidth=2)
ax.plot(tspan_1, rho, color='k')
ax.plot(tspan_2, rho2, color='k', linestyle='dashed')

#plt.plot(15.1, 0.9649, 'go')
#plt.xlim([5, 27])
#plt.ylim([0.92, 0.99])
ax.set_xlabel(r'$t-t_i$', color="k", fontsize=25)
plt.ylabel(r'$\rho/\varepsilon^4$', color="k", fontsize=25)
ax.tick_params(axis='x',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
ax.tick_params(axis='y',which='major',direction='in',length=5,width=1,color='black',pad=15,labelsize=15,labelcolor='black')
#ax.minorticks_on()
plt.tight_layout()
plt.savefig('density')
plt.show()

 



# show the plot
plt.show()


