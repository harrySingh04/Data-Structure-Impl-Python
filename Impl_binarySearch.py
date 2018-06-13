class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setLeft(self,left):
        self.left = left

    def getLeft(self):
        return self.left

    def setRight(self,right):
        self.right = right

    def getRight(self):
        return self.right

class BinaryTree:

    def __init__(self):
        self.root = None

    #Iterative method of adding the node in the tree
    # Assuming every data entered in the binary data is different.
    def insert(self,data):
        newNode = TreeNode(data)
    # If root is None that means tree is empty so we will
    # add the node directly to the tree
        if self.root == None:
            self.root = newNode
            return
        current = self.root
        prev = self.root
        while(current!=None):
            if current.getData()>data:
                prev = current
                current = current.getLeft()
            elif current.getData()<data:
                prev = current
                current = current.getRight()
            else:
                print("Data already present in the binary tree.")
                return
        if prev.getData()>data:
            prev.setLeft(newNode)
        else:
            prev.setRight(newNode)

    # Recursive way of inserting the element in the Binary Tree
    def insertRecur(self,data,current):
        if self.current == None:
            current = TreeNode(data)
        else:
            if current.getData()>data:
                current.setLeft(insertRecur(data,current.getLeft()))
            elif current.getData() < data:
                current.setRight(insertRecur(data,current.getRight()))

        return current

    # Iterative way of searching the item
    def search(self,item):
        current = self.root
        if(root==None):
            print("Tree is empty!!")
        while(current!=None):
            if current.getData()>item:
                current = current.getLeft()
            elif current.getData()<item:
                current = current.getRight()
            else:
                print("Item is found!!!")
                return
        print("Item is not found!!!")

    # Recursive method of searching the Item
    def searchRecur(self,item,current):
        if current == None:
            print("Item not found")
        else:
            if current.getData()>item:
                searchRecur(self,item,current.getLeft())
            elif current.getData()<item:
                searchRecur(self,item,current.getRight())
            else:
                print("Item is found ")
    # Iteratve way of Inorder traversal
    def inorder(self):
        s = []
        current = self.root
        if(current==None):
            print("Tree is Empty")
        else:
            s = []
            while(current!=None or len(s)!=0):
                if current!=None:
                    s.append(current)
                    current = current.getLeft()
                else:
                    temp = s.pop()
                    print(temp.getData())
                    current = temp.getRight()


    # Recursive way of inorder traversal
    def inorderTree(self,current):
        if current==None:
            return
        else:
            self.inorderTree(current.getLeft())
            print(current.getData())
            self.inorderTree(current.getRight())
    # Iterative way of preorder traversal
    def preorder(self):
        current = self.root
        if current==None:
            print("Tree is Empty")
        else:
            s = []
            while(current!=None or len(s)!=0):
                if current!=None:
                    print(current.getData())
                    s.append(current)
                    current = current.getLeft()
                else:
                    current = s.pop().getRight()
    # # Display binary tree as a graphical way in a tree format
    # def displayTree(self):
    #     if self.root == None:
    #         print(" TREE IS EMPTY!!!!!!!")
    #     else:
    #         print("----------ROOT OF THE TREE----------")
    #         print()
    #         print()
    #         print("     -----"+str(self.root.getData())+"-----        ")
    #         leftTree = self.root.getLeft()
    #         rightTree = self.root.getRight()
    #         current = self.root
    #         print("     |          |")
    #         print("     |          |")
    #         print("     |          |")
    #         while(current!=None):
    #             if(current.getLeft()!=None):
    #                 leftTree==current.getLeft()
    #             else:
    #                 leftleft = None
    #             if(leftTree!=None):
    #                 print("    "+str(leftTree.getData()),end="")
    #             if(current.getRight()!=None):
    #                 rightTree==current.getRight()
    #             else:
    #                 rightleft = None
    #             if(rightTree!=None):
    #                 print("    "+str(rightTree.getData()),end="")
    #
    #
    #


    # Recursive way of preorder traversal
    def preorderTree(self,current):
        if current==None:
            return
        else:
            print(current.getData())
            self.preorderTree(current.getLeft())
            self.preorderTree(current.getRight())
    # Postorder Traversal in iterative way
    def postOrder(self):
        current = self.root
        if current == None:
            print("Tree is Empty")
        else:
            s = []
            while(len(s)!=0 or current!=None ):
                if current!=None:
                    if current.getRight()!=None:
                        s.append(current.getRight())
                    s.append(current)
                    current = current.getLeft()

                else:
                    temp = s.pop()
                    temp2 = temp.getRight()
                    size = len(s)
                    if temp2==None:
                        print(temp.getData())
                    if temp2!=None:
                        if size>0:
                            if temp2==s[-1]:
                                current = s.pop()
                                s.append(temp)
                            else:
                                print(temp.getData())
                                current = None
                        else:
                            print(temp.getData())
                            current = None


    # Recursive way of postorder traversal
    def postorderTree(self,current):
        if current==None:
            return
        else:
            self.postorderTree(current.getLeft())
            self.postorderTree(current.getRight())
            print(current.getData())
