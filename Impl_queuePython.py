class Queue:
    def __init__(self):
        #Initiliazing the list for the queue operation
        self.items = []

    def enqueue(self,item):
        #Adding the item into the queue list
        #print("i am here")
        self.items.append(item)

    def dequeue(self):
        #Removing the item from the queue list

        if not self.isEmpty():
            remove_item = self.items[0]
            self.items.pop(0)
            return remove_item
        else:
            #Underflow of the Queue
            return None

    def isEmpty(self):
        #Check if the queue is empty or not
        return len(self.items) == 0

    def size(self):
        #Checking the size of the queue list
        return len(self.items)
