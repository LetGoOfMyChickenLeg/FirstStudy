from pandas import Series
from pandas import read_table

A = Series([1, 2, 3], index = [1, 2, 3])
print(A)

df = read_table(r"DataOfreadtable.txt", sep="\s+")
print(df.head())
