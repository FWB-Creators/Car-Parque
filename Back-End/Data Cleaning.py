import numpy as np
import pandas as pd

df = pd.read_csv("/Users/suchanatratanarueangrong/Hackaday/Mall mock data.csv")
df = df[['Mall Location', 'Latitude', 'Longitude']].drop_duplicates('Mall Location')
# print(df.head(50))
df.to_json("Mall_Name_lat_long.json")
# df.to_csv("Mall_Name_lat_long.csv")