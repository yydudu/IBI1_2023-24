import numpy as np
import matplotlib.pyplot as plt

population = np. zeros ( (100 , 100) )
beta=0.3
gamma=0.05
time_steps=100

centerx,centery=np.random.randint(0,100,2)
population[centerx,centery]=1

snapshots={t:None for t in [0,10,50,time_steps-1]}

for time in range(time_steps):
    new=population.copy()
    for row in range(100):
        for col in range(100):
            if population[row,col]==1:
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr==0 and dc==0:
                            continue
                        r=row+dr
                        c=col+dc
                        if 0<=r<100 and 0<=c<100:
                            if population[r,c]==0 and np.random.random()<beta:
                                new[r,c]=1
                if np.random.random()<gamma:
                    new[row,col]=2
    population=new
    if time in snapshots:
        snapshots[time]=population.copy()

fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,7))
for ax,(t,snapshot) in zip(axes.flat,snapshots.items()):
    ax.imshow(snapshot,cmap='viridis',interpolation='nearest')
    ax.set_title(f'State of Population at Time {t}')
    ax.axis('off')

plt.tight_layout()
plt.show()
plt.clf
