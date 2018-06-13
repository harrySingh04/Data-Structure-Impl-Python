class Node:
    """Implementation of Node class"""
    def __init__(self,data):
    # Constructor to intialize the this object
        self.data = data
    # Next pointer for reference to the next item in the list
        self.next = None

    def getData(self):
    # Getter method for data variable
        return self.data

    def setData(self,data):
    # Setter method for the data variable
        self.data = data

    def getNext(self):
    # Getter method for the Next variable
        return self.next

    def setNext(self,next):
    # Setter method for the data variable
        self.next = next

class SingleLinkedList:
    """Implementation of Single Linked List methods"""
    def __init__(self):
        # intialize the head  Linked list
        self.head = None
        #self.tail = None

    def _size(self):
        # Calculate Length of the linked list
        current = self.head
        index = 0
        while(current!=None):
            index = index + 1
            current = current.getNext()
        return index

    def _search(self,data):
        # Search of the data into the linked list
        if self.head==None:
            # if list is empty then return None
            print("List is Empty")
            return None
        # If there is data in the list then search for the data in the linked list
        current = self.head
        while(current!=None):
            if current.getData()==data:
                # if data found then return that node
                print("Element found")
                return current
            else:
                current = current.getNext()
        # if data not found then return None
        print("Element not in the list")
        return None


    def _addFirstNode(self,item):
        # add the node in the first position of the list
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode
    def _addLastNode(self,item):
        # add the item in the last position of the linked list
        newNode = Node(item)
        current = self.head
        #print("data here= ",current.data)
        while(current.getNext()!=None):
            current  = current.getNext()
        current.setNext(newNode)

    def _addInBetween(self,item,index):
        # add the item at the value of the index given.(if index is 4 then new item will
        #be added in between index 4 and 5)
        newNode = Node(item)
        curIndex = 0
        current = self.head
        while(current!=None and index!=curIndex):
            current = current.getNext()
            curIndex=curIndex+1
        # If position found for insertion then insert the element
        if(current!=None):
            temp = current.getNext()
            current.setNext(newNode)
            newNode.setNext(temp)

    def _add(self,item,index):
        # Adding the item into the linked list
        if index==0:
            self._addFirstNode(item)
        elif index == self._size()-1:
            self._addLastNode(item)
        else:
            self._addInBetween(item,index)

    def _removeFirst(self):
        # Remove the first item from the linked list
        self.head = self.head.getNext()

    def _removeLast(self):
        # Remove the last item from the linked list
        current = self.head
        temp = current
        while(current.getNext()!=None):
            temp = current
            current = current.getNext()
        temp.setNext(None)

    def _removeInBetween(self,index):
        # Remove the item in between the list
        current = self.head
        curIndex = 0
        temp = current
        while(current!=None and curIndex!=index):
            curIndex = curIndex + 1
            temp = current
            current = current.getNext()
        if(current!=None):
            temp.setNext(current.getNext())

    def _remove(self,index):
        # Removing item from the linked list
        if index == 0:
            self._removeFirst()
        elif index==self._size():
            self._removeLast()
        else:
            self._removeInBetween(index)

    def _displayList(self):
        # Displaying the items of the linked list

        current = self.head
        if(current==None):
            # If there is no element then print list is empty
            print("List is Empty")
        else:
            print("Single List data is:")
            while(current!=None):
                print(current.getData())
                current = current.getNext()
