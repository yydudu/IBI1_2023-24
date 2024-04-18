# import necessary librairies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N=1000
V=0.1
beta = 0.3
gamma =0.05

vaccination_rates=[i/10 for i in range(11)]

infected_dict={}

for v_rate in vaccination_rates:
    S=N-1-int(N*v_rate)
    I=1
    R=0
    I_arrays=[I]
    S_arrays=[S]
    R_arrays=[R]
    for i in range(1000):
        if S > 0:
            infect_prob = beta * I / (N - V)
            new_infection = np.random.binomial(S, infect_prob)
        else:
            new_infection = 0

        if I > 0:
            new_recovery = np.random.binomial(I, gamma)
        else:
            new_recovery = 0
    
        S -= new_infection
        I += new_infection - new_recovery
        R += new_recovery
        S = max(S, 0)
   
        S_arrays.append(S)
        I_arrays.append(I)
        R_arrays.append(R)

    infected_dict[v_rate]=I_arrays

plt.figure(figsize =(6 ,4) , dpi=150)
for v_rate, I_arrays in infected_dict.items():
    plt.plot(I_arrays, label=f'Vaccination Rate: {v_rate*100}%')

plt.xlabel('Time (days)')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Vaccintaion')
plt.legend()

plt.savefig('C:/Users/huawei/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical10/SIR figure vaccinated.png')
plt.show()
plt.clf


