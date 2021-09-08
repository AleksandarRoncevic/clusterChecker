import networkx as nx

def checkCoalition(mainGraph : nx.Graph, cluster : nx.Graph):
    badLinks = []
    for u in cluster.nodes():
        for v in cluster.nodes():
            if(u == v):continue
            if not(mainGraph.has_edge(u,v)): continue

            weight = mainGraph.get_edge_data(u,v)["weight"]
            if(weight == 0):
                badLinks.append({u,v})
    if not(badLinks) :
        return { "status" : True }
    else:
        return { "status" : False, "edge" : badLinks}
