class DisJointSet(object):

    def __init__(self):
        self.mapSet = {}

    def makeSet(self,data):

        newNode = Node(data)
        #Initially setting parent to itself.
        newNode.parent = newNode
        
        #Add new node in the dictionary.
        self.mapSet[data] = newNode
        #print(self.mapSet[data].parent.data)
    
    def unionSet(self,data1,data2):
        node1 = self.mapSet[data1]
        node2 = self.mapSet[data2]

        parent1 = self.findSet(node1)
        parent2 = self.findSet(node2)

        if(parent1 == parent2):
            return
        else:
            if(parent1.rank>=parent2.rank):
                parent1.rank = parent1.rank+1 if parent1.rank==parent2.rank else parent1.rank
                parent2.parent = parent1
            else:
                parent1.parent = parent2
        

        
    def findSet(self,node1):
        #print(type(node1))
        if(node1.parent.__eq__(node1)):
            return node1.parent
        else:
            node1.parent = self.findSet(node1.parent)
            return node1.parent

    def find(self,data):
        return self.findSet(self.mapSet[data]).data


class Node(object):

    def __init__(self,data):
        self.data = data
        self.rank = 0
        self.parent = None
    
    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)
    

