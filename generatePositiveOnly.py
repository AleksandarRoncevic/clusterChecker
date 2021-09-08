import networkx as nx

def generatePositiveOnly(G : nx.Graph):
    H : nx.Graph = nx.create_empty_copy(G)
    for u,v,a in G.edges(data=True) :
        if(a["weight"] > 0) :
            H.add_edge(u,v,weight=a["weight"])
    return H




