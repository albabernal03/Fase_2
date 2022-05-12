import pwd
import pandas as pd
import os
import re

x= %pwd #para ver la ruta de trabajo
print(x)

path= '/Users/hectorbernaltrujillo/Documents/informática/Programación python/Fase_2/archive (3)/ETFs'
os.chdir(path)
y= %pwd #para ver la ruta de trabajo
print(y)

archivos= [ x for x in os.listdir() if re.search('.txt',x)]
print(archivos)

df= pd.DataFrame()
for i in archivos:
    archivo=pd.read_csv(i)
    df= pd.concat([df,archivo])
    df.to_csv('datos_archivos.csv')
    


    





