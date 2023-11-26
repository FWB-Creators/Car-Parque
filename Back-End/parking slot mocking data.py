import pandas as pd
import numpy as np
import random

df = pd.DataFrame(columns=['Mall_name','Floor','Floor_slot','Empty'])
for i in range(1,51):
    df.loc[i, 'Floor'] = 1
    df.loc[i, 'Mall_name'] = "Siam Paragon"
    df.loc[i, 'Floor_slot'] = i
    df.loc[i, 'Empty'] = bool(random.randint(0, 1))
for i in range(1,51):
    df.loc[i+50, 'Floor'] = 2
    df.loc[i+50, 'Mall_name'] = "Siam Paragon"
    df.loc[i+50, 'Floor_slot'] = i
    df.loc[i+50, 'Empty'] = bool(random.randint(0, 1))
for i in range(1,41):
    df.loc[i+100, 'Floor'] = 3
    df.loc[i+100, 'Mall_name'] = "Siam Paragon"
    df.loc[i+100, 'Floor_slot'] = i
    df.loc[i+100, 'Empty'] = bool(random.randint(0, 1))

for i in range(1,51):
    df.loc[i+140, 'Floor'] = 1
    df.loc[i+140, 'Mall_name'] = "MBK Center"
    df.loc[i+140, 'Floor_slot'] = i
    df.loc[i+140, 'Empty'] = bool(random.randint(0, 1))
for i in range(1,41):
    df.loc[i+190, 'Floor'] = 2
    df.loc[i+190, 'Mall_name'] = "MBK Center"
    df.loc[i+190, 'Floor_slot'] = i
    df.loc[i+190, 'Empty'] = bool(random.randint(0, 1))
    
for i in range(1,31):
    df.loc[i+230, 'Floor'] = 1
    df.loc[i+230, 'Mall_name'] = "Central Embassy"
    df.loc[i+230, 'Floor_slot'] = i
    df.loc[i+230, 'Empty'] = bool(random.randint(0, 1))

for i in range(1,51):
    df.loc[i+260, 'Floor'] = 1
    df.loc[i+260, 'Mall_name'] = "Samyan Mitrtown"
    df.loc[i+260, 'Floor_slot'] = i
    df.loc[i+260, 'Empty'] = bool(random.randint(0, 1))

for i in range(1,21):
    df.loc[i+310, 'Floor'] = 2
    df.loc[i+310, 'Mall_name'] = "Samyan Mitrtown"
    df.loc[i+310, 'Floor_slot'] = i
    df.loc[i+310, 'Empty'] = bool(random.randint(0, 1))

for i in range(1,51):
    df.loc[i+330, 'Floor'] = 1
    df.loc[i+330, 'Mall_name'] = "CentralWorld"
    df.loc[i+330, 'Floor_slot'] = i
    df.loc[i+330, 'Empty'] = bool(random.randint(0, 1))
for i in range(1,41):
    df.loc[i+380, 'Floor'] = 2
    df.loc[i+380, 'Mall_name'] = "CentralWorld"
    df.loc[i+380, 'Floor_slot'] = i
    df.loc[i+380, 'Empty'] = bool(random.randint(0, 1))
for i in range(1,11):
    df.loc[i+420, 'Floor'] = 3
    df.loc[i+420, 'Mall_name'] = "CentralWorld"
    df.loc[i+420, 'Floor_slot'] = i
    df.loc[i+420, 'Empty'] = bool(random.randint(0, 1))
df.to_json("Mall parking slot.json")
df.to_csv("Mall parking slot.csv")

print(df.count())
