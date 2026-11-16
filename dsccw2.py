import numpy as np

nparr=np.arange(1,501,2)
#print(nparr)

nparr2=np.linspace(0,10,4)
#print(nparr2)

nparr3=np.arange(1,11)
#print(nparr3)
#print(nparr3.shape)

nparr4=nparr3.reshape(2,5)
#print(nparr4)

#print(np.random.permutation(nparr3))

nparr6=np.random.randint(1,50,10)
nparr6half=np.random.randint(1,50,(5,2))
#print(nparr6)
#print(nparr6half)

nparr7=np.sort(nparr6)
#print(nparr7)
nparr7half=np.sort(nparr6half)
#print(nparr7half)

nparr8=nparr6[1:9]
#print(nparr8)