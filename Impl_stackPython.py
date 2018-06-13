class stack:
    def __init__(self):
        #Initiliazing the list for the stack operation
        self.items = []
        self.top = -1
    def push(self,item):
        #Pushing the items into the list
        self.items.append(item)
        self.top = self.top+1
    def isEmpty(self):
        #Return True if list is empty or else false
        return self.items == []
    def pop(self):
        #Check if there is item in the stack list
        if not self.isEmpty():
            # Saving the last item to be removed in the variable
            remove_item = self.items[-1]
            self.items.pop()
            return remove_item
        else:
            #Stack Underflow
            return None
    def size(self):
        #Returning the size of the stack list
        return len(self.items)
    def peek(self):
        #Returning the top element without removing it
        return self.items[len(self.items)-1]
