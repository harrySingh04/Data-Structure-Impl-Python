from Graph import graph
import Impl_disjointSet

def implement_krusal(g):
    edges = []
    nodes = []
    DJSet = Impl_disjointSet.DisJointSet()

    edges = g.get_all_edges()
    edges = sorted(edges,key=edge_sort)
    for i in range(len(edges)):
        print(edges[i])
        if edges[i].from_node not in nodes:
            nodes.append(edges[i].from_node)

        if edges[i].to_node not in nodes:
            nodes.append(edges[i].to_node)

    for i in range(len(nodes)):
        DJSet.makeSet(nodes[i].data)

    mst_edges=[]
    for edge in edges:
        parent1 =DJSet.find(edge.from_node.data)
        parent2 =DJSet.find(edge.to_node.data)
        if(parent1!=parent2):
            mst_edges.append(edge)
            DJSet.unionSet(edge.from_node.data,edge.to_node.data)

    #print(mst_edges)
        
            
    

        

            
        

def edge_sort(edge):
    return edge.weight
