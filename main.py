from generateNetClusters import generateNetClusters
import networkx as nx
from generateConnectedComponents import generateComponents
from generatePositiveOnly import generatePositiveOnly
from checkIfCoalition import checkCoalition
import random


G : nx.Graph = nx.gnp_random_graph(12,0.4)
F : nx.Graph= nx.empty_graph(12)

for e in G.edges():
    F.add_edge(e[0],e[1],weight= 1 if(random.random()*10 >= 5) else 0 )


F_positive : nx.Graph = generatePositiveOnly(F)
print("Positive edges only:")
print(F_positive.edges.data())

AllCluster : set = generateComponents(F_positive)
GoodCluster = []
BadCluster = []
isClusterable : bool = True
badLinks = []

for cluster in AllCluster:
    result = checkCoalition(F,cluster)
    if(result["status"] == False):
        isClusterable= False
        BadCluster.append(cluster)
        for el in result["edge"]:
            badLinks.append(el)
    else:
        GoodCluster.append(cluster)
        
    

print("Mreza je klasterabilna" if isClusterable else "Mreza nije klasterabilna" )
print("\n")

uniqueBadLinks = []
for el in badLinks:
    if el not in uniqueBadLinks:
        uniqueBadLinks.append(el)

print("Linkovi koji kvare klasterabilnost su: ", uniqueBadLinks)
print("\n")

print("Klasteri koji nisu koalicije: ")
i=0
for cluster in BadCluster:
    print(BadCluster[i].nodes())
    i = i + 1

i=0
print("\n")
print("Klasteri koji jesu koalicije: ")
for cluster in GoodCluster:
    print(GoodCluster[i].nodes())
    i = i + 1

print("\n")
netOfClusters : nx.Graph = generateNetClusters(AllCluster,uniqueBadLinks,F)
print("Mreza klastera odnosno cvorovi mreze: ")
print(netOfClusters.nodes.data())