import pandas as pd
import numpy
import ClusterAddresses
import distance_matrix
import shortest

### This program is part of Dynamic waste collection Bachelors thesis
### The main purpose of this is to create a simulation of dynamic and static waste collection
### and produce numeral values for effiency of logistics in both scenarios

def main():
    ### Open data containing 19k adresses from the city of Lappeenranta
    ### https://www.avoindata.fi/data/fi/dataset/postcodes

    dataframe = pd.read_csv('Lappeenranta.csv')
    results = numpy.array([["Type", "Route length", "Average speed"]])

    for i in range(0,5):
        print(i)
        df = newDataframe(dataframe, i)
        results = getResults(df, results, i)
        file = open("results.txt", "w+")
        file.write(str(results))
        file.close()
    return
    


def newDataframe(dataframe, i):
    sample = dataframe.sample(5000)
    df = ClusterAddresses.clustering(sample, i)
    return df


def getResults(df, results, runcount):
        ## Route for each day of the week
    cluster_1 = df.loc[df['cluster_label'] == 0]
    cluster_2 = df.loc[df['cluster_label'] == 1]
    cluster_3 = df.loc[df['cluster_label'] == 2]
    cluster_4 = df.loc[df['cluster_label'] == 3]
    cluster_5 = df.loc[df['cluster_label'] == 4]
    

    ## Testing
    print(len(cluster_1.index))
    print(len(cluster_2.index))
    print(len(cluster_3.index))
    print(len(cluster_4.index))
    print(len(cluster_5.index))
    
    if(len(cluster_1.index) >= 75):  
        for i in range(0, 10): 
                    name = str(runcount)+"_cluster_1_"+str(i)+".html"
                    distance, duration, dfn = distance_matrix.distancematrix(cluster_1.sample(75))
                    dist, sped = shortest.shortestp(distance, duration, dfn, name)
                    results = numpy.append(results, [["Monday", dist, sped ]], axis = 0)
                    print(results)
    if(len(cluster_2.index) >= 75):   
        for i in range(0, 10):
                    name = str(runcount)+"_cluster_2_"+str(i)+".html"
                    distance, duration, dfn = distance_matrix.distancematrix(cluster_2.sample(75))
                    dist, sped = shortest.shortestp(distance, duration, dfn, name)
                    results = numpy.append(results, [["Tuesday", dist, sped]], axis = 0)
                    print(results)
    if(len(cluster_3.index) >= 75):    
        for i in range(0, 10):
                    name = str(runcount)+"_cluster_3_"+str(i)+".html"
                    distance, duration, dfn = distance_matrix.distancematrix(cluster_3.sample(75))
                    dist, sped = shortest.shortestp(distance, duration, dfn, name)
                    results = numpy.append(results, [["Wednesday", dist, sped]], axis = 0)
                    print(results)
    if(len(cluster_4.index) >= 75):
        for i in range(0, 10):
                    name = str(runcount)+"_cluster_4_"+str(i)+".html"
                    distance, duration, dfn = distance_matrix.distancematrix(cluster_4.sample(75))
                    dist, sped = shortest.shortestp(distance, duration, dfn, name)
                    results = numpy.append(results, [["Thursday", dist, sped]], axis = 0)
                    print(results)
    if(len(cluster_5.index) >= 75):
        for i in range(0, 10):
                    name = str(runcount)+"_cluster_4_"+str(i)+".html"
                    distance, duration, dfn = distance_matrix.distancematrix(cluster_5.sample(75))
                    dist, sped = shortest.shortestp(distance, duration, dfn, name)
                    results = numpy.append(results, [["Thursday", dist, sped]], axis = 0)
                    print(results)
    for i in range(0, 30):
                name = str(runcount)+"_dynamic_"+str(i)+".html"
                distance, duration, dfn = distance_matrix.distancematrix(df.sample(75))
                dist, sped = shortest.shortestp(distance, duration, dfn, name)
                results = numpy.append(results, [["Dynamic route", dist, sped]], axis = 0)
                print(results)
    return results

main()