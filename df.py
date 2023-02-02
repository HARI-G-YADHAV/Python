import pandas as pd
data = pd.read_csv("Students.csv")
print("Read marks between 80 and 90")
df1 = data["marks"].between(80,90,"both")
print(data[df1].iloc[:,[1]])
print("exclude 90 and 80")
df2 = data["marks"].between(80,90,"neither")
print(data[df2])
