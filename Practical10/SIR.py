# import necessary librairies
import numpy as np
import matplotlib.pyplot as plt


N=1000
I=1
R=0
S=N-I-R
beta = 0.3
gamma =0.05

S_arrays=[S]
R_arrays=[R]
I_arrays=[I]

for i in range(1000):
    infect_prob = beta*I/N
    recovery_prob = gamma
    infection=np.random.choice([0,1],size=S,p=[1-infect_prob,infect_prob])
    newinfection=np.sum(infection)

    recovery=np.random.choice([0,1],size=I,p=[1-gamma,gamma])
    newrecovery=np.sum(recovery)
    S-=newinfection
    I+=newinfection-newrecovery
    R+=newrecovery

    S_arrays.append(S)
    I_arrays.append(I)
    R_arrays.append(R)

plt.figure(figsize =(6 ,4) , dpi=150)
plt.plot(S_arrays,label='susceptible')
plt.plot(I_arrays,label='infected')
plt.plot(R_arrays,label='recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend()

plt.savefig('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical10/SIR figure.png')
plt.show()
plt.clf