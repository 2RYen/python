import random

time_100=[0]*46
time_1000=[0]*46
time_10000=[0]*46

for cnt1 in range(100):
    x=random.randint(1,45)
    time_100[x]=time_100[x]+1

for cnt1 in range(1000):
    x=random.randint(1,45)
    time_1000[x]=time_1000[x]+1

for cnt1 in range(10000):
    x=random.randint(1,45)
    time_10000[x]=time_10000[x]+1

for k in range(1,46):
  print(k,100*time_100[k]/100,100*time_1000[k]/1000,100*time_10000[k]/10000)
