import pwd
import pandas as pd
import os
import re

def ruta_trabajo():
    x= %pwd #para ver la ruta de trabajo
    return x
ruta_trabajo()

def ruta_carpeta_ETFs():
    path= '/Users/hectorbernaltrujillo/Documents/informática/Programación python/Fase_2/archive (3)/ETFs'
    os.chdir(path)
    y= %pwd #para ver la ruta de trabajo
    return y
ruta_carpeta_ETFs

def union_archivos_ETFs(path):
    archivos= [ x for x in os.listdir() if re.search('.txt',x)]
    print(archivos)
    df= pd.DataFrame()
    for i in archivos:
        archivo=pd.read_csv(i)
        df= pd.concat([df,archivo])
        df.to_csv('datos_archivo_ETFs.csv')
    return df
union_archivos_ETFs(ruta_carpeta_ETFs())





