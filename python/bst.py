insert_count = 0

class Tree(object):
    def __init__(self, data=None, comp_func=None):
        self.left = None
        self.right = None
        self.data = data
        if comp_func:
            self.compare = comp_func

    def insert(self, data, root=None):
        global insert_count
        if root == None:
            if insert_count == 0: # forced
                print insert_count
            root = Tree(data)
            insert_count += 1
            print insert_count
        elif root.data == None:
            root.data = data
        elif root.compare(data) == -1:
            root.left = self.insert(data, root.left)
        elif root.compare(data) == 1:
            root.right = self.insert(data, root.right)

        return root

    def compare(self, data):
        if self.data > data:
            return -1
        if self.data < data:
            return 1
        return 0

def createBST(keys):
    root = Tree()
    for key in keys:
        root = root.insert(data=key, root=root)

    print insert_count


if __name__ == '__main__':
    key_count = int(raw_input())

    keys = []
    for _ in xrange(key_count):
        key_item = int(raw_input())
        keys.append(key_item)

    createBST(keys)
