import networkx as nx

def generateComponents(G : nx.Graph):

    def identifyComponent(start_node):
        component= set()
        component.add(start_node)
        
        visited.add(start_node)
        dfs(start_node,component)
        return frozenset(component)

    def dfs(curr,component : set):
        for adjacentNode in G.adj[curr]:
            if not(visited.__contains__(adjacentNode)):
                component.add(adjacentNode)
                visited.add(adjacentNode)
                dfs(adjacentNode,component)

    visited = set()
    components  = set()
    for u in G.nodes():
        if not(visited.__contains__(u)):
            components.add(identifyComponent(u))

    componentsCluster = []
    for comp in components:
        H = G.subgraph(comp).copy()
        componentsCluster.append(H)
    return componentsCluster



