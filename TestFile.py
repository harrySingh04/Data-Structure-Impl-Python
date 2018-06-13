import Impl_binarySearch as BinaryTree
import Impl_disjointSet as DisJointSet
from Graph import graph
import Impl_Krusal_Algo as mst

'''bst = BinaryTree.BinaryTree()
bst.insert(16)
bst.insert(21)
bst.insert(11)
bst.insert(14)
bst.insert(6)
bst.insert(8)
bst.insert(7)
bst.insert(9)
bst.insert(13)
#bst.displayTree()
bst.postorderTree(bst.root)
print()
print("Iterative way")
bst.postOrder()
'''
# Testing the Disjoint Functionality

'''set = DisJointSet.DisJointSet()
		
set.makeSet(1)
set.makeSet(2)
set.makeSet(3)
set.makeSet(4)
set.makeSet(5)
set.makeSet(6)
set.makeSet(7)
		
set.unionSet(1, 2)
set.unionSet(2, 3)
set.unionSet(4, 5)
set.unionSet(6, 7)
set.unionSet(5, 6)
set.unionSet(3, 7)
		
print(set.find(1))
print(set.find(2))
print(set.find(3))
print(set.find(4))
print(set.find(5))
print(set.find(6))
print(set.find(7))
'''
graph_1_path = './File/graph-1.txt'
graph_1 = graph.construct_graph_from_file(graph.AdjacencyList(), graph_1_path)

mst.implement_krusal(graph_1)

