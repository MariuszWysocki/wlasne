import random
import quantumrandom
import time



# rnd  = random.SystemRandom()
# for i in range (16):
#     losuje = rnd.sample(range(11,48),6)
#     print(losuje)

rmg = quantumrandom
a = rmg.get_data()
print(a)