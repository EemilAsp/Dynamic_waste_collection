import requests
import numpy as np


def distancematrix(df):
    df.loc[-1] = ['0', 'Mäntysuonkatu', '13', '53550','61.03701916', '28.195390692', '0']
    apicall = ""
    for i in df.index:
        apicall += ";"+str(df['Y'][i])+","+str(df['X'][i])
    
    apicall = apicall[1:]
    
    # This url is for the online api, but during this project i used
    # locally hosted instance of OSRM 
    matrixurl = 'http://router.project-osrm.org/table/v1/driving/'+apicall+'?annotations=duration,distance'

    r = requests.get(matrixurl)
    res = r.json()
    ##print("matrix")
    ##for data in res['sources']:
        ##print(data['name'])
    ##print("dataframe")
    ##for data in df.index:
        ##print(df['Osoite'][data])
    Distancearray = np.array(res['distances'])
    Durationarray = np.array(res['durations'])

    return Distancearray, Durationarray, df

