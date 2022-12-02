import os
os.environ["OMP_NUM_THREADS"] = '2'
from sklearn.cluster import KMeans
import folium
import folium.plugins as plugins
from sklearn.metrics import silhouette_score


def optimalClusters(df): ## not used
    sil_score_max = -1
    lista = df.loc[:,['X', 'Y']]
    for n_clusters in range(2,10):
        model = KMeans(n_clusters = n_clusters, init='random', max_iter=100, n_init=1)
        labels = model.fit_predict(lista[lista.columns[1:2]])
        sil_score = silhouette_score(lista[lista.columns[1:2]], labels)
        if sil_score > sil_score_max:
            sil_score_max = sil_score
            best_n_clusters = n_clusters
    return best_n_clusters


def clustering(dataframe, runcount):

    clusters=folium.Map()
    clusters2=folium.Map()

    sample = dataframe.sample(500)

    cluster_n = optimalClusters(sample)

    for ind in sample.index:
        icon2 =plugins.BeautifyIcon(border_color='#7F8C8D',text_color='#000000', inner_icon_style='margin-top:0;')
        folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters)

    ##clusters.save("unclustered_"+str(runcount)+".html")
    lista = sample.loc[:,['Index', 'X', 'Y']]

    kmeans = KMeans(n_clusters = 3, init ='random', n_init=50)
    kmeans.fit(lista[lista.columns[1:3]])
    lista['cluster_label'] = kmeans.fit_predict(lista[lista.columns[1:3]])

    sample = sample.join(lista['cluster_label'])
    for ind in sample.index:
        if(str(sample['cluster_label'][ind]) == '0'):
            icon2 =plugins.BeautifyIcon(border_color='#7F8C8D',text_color='#000000', number=int(sample['cluster_label'][ind]), inner_icon_style='margin-top:0;')
            folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters2)
        if(str(sample['cluster_label'][ind]) == '1'):
            icon2 =plugins.BeautifyIcon(border_color='#F1C40F',text_color='#000000', number=int(sample['cluster_label'][ind]), inner_icon_style='margin-top:0;')
            folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters2)
        if(str(sample['cluster_label'][ind]) == '2'):
            icon2 =plugins.BeautifyIcon(border_color='#2874A6',text_color='#000000', number=int(sample['cluster_label'][ind]), inner_icon_style='margin-top:0;')
            folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters2)
        if(str(sample['cluster_label'][ind]) == '3'):
            icon2 =plugins.BeautifyIcon(border_color='#2874A6',text_color='#000000', number=int(sample['cluster_label'][ind]), inner_icon_style='margin-top:0;')
            folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters2)
        if(str(sample['cluster_label'][ind]) == '4'):
            icon2 =plugins.BeautifyIcon(border_color='#2874A6',text_color='#000000', number=int(sample['cluster_label'][ind]), inner_icon_style='margin-top:0;')
            folium.Marker(location=[sample['X'][ind],sample['Y'][ind]], icon = icon2).add_to(clusters2)

    return (sample)



