class BinarySearchTree:
    # self is a node    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check where it fits 
        if value >= self.value:
        # look right
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            # if less
            # look left
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            # look right
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else: 
                return False

