from python_tsp.heuristics import solve_tsp_simulated_annealing
from sys import maxsize
import requests
import polyline
import folium
import folium.plugins as plugins



def shortestp(matrix, distm, df, name):
    map_new=folium.Map()
    distance = maxsize
    numbers = list(range(0,len(df.index)))
    permutation = []
    distancearr = []
    durationarr = []
    df['ind'] = numbers

    apicall = ''
    
    for i in range (1):
        perm, d1 = solve_tsp_simulated_annealing(matrix)
        if(d1 < distance):
            distance = d1
            permutation = perm

    for i in range (0,len(permutation)):
        distancearr.append(matrix[permutation[i]][permutation[i-1]])
        durationarr.append(distm[permutation[i]][permutation[i-1]])

    df['order'] = permutation
    distance = distance / 1000
    for i in range(0, len(permutation)):
        df.loc[df['ind'] == permutation[i], "order"] = i    
              
    df = df.sort_values(by=['order'])

    for i in df.index:
        apicall += ";"+str(df['Y'][i])+","+str(df['X'][i])
    apicall += ";"+str(df['Y'].iat[0])+","+str(df['X'].iat[0])
    apicall = apicall[1:]
    curl = 'http://router.project-osrm.org/route/v1/driving/'+apicall+'?overview=full&continue_straight=false'
    r = requests.get(curl)
    res = r.json()
    routes=polyline.decode(res['routes'][0]['geometry'])
    route = {'route':routes}
    folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(map_new)

    for i in range(0,len(df)):
        loc = [df.iloc[i]['X'], df.iloc[i]['Y']]
        if loc == ['61.03701916','28.195390692']:
            icon2 =plugins.BeautifyIcon(border_color='#ff0000',
                        text_color='#ff0000', number=int(df.iloc[i]['order']), inner_icon_style='margin-top:0;')
        else:
            icon2 = plugins.BeautifyIcon(border_color='#00ABDC',
                        text_color='#00ABDC', number=int(df.iloc[i]['order']), inner_icon_style='margin-top:0;')
        folium.Marker(location=loc, icon=icon2).add_to(map_new)
    
    averagespeed = round((distance / ((sum(durationarr) * 0.000277777778))))
    ##map_new.save(name)
    print("##############################################")
    print("Route length in kilometers: "+str(round(distance,2)))
    print("Average speed during tour: "+str(averagespeed)+" km/h")
    

    return (round(distance,2), averagespeed)