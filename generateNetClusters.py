import networkx as nx

def generateNetClusters(clusters, badLinks, mainGraph : nx.Graph):
    
    clusterNodes : nx.Graph = nx.empty_graph(len(clusters))
    for i in range(len(clusters)):
        clusterNodes.nodes[i]["cluster"] = clusters[i]

    for badLink in badLinks:
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                nodes = []
                for node in badLink:
                    nodes.append(node)
                if((nodes[0] in clusters[i] or nodes[0] in clusters[j]) and 
                (nodes[1] in clusters[i] or nodes[1] in clusters[j]) and 
                mainGraph.has_edge(nodes[0],nodes[1])):
                    clusterNodes.add_edge(i,j)
    return clusterNodes


                

                    
                





