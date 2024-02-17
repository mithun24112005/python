import pandas as pd

simp=pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
len=len(simp)
print(len)