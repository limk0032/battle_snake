class TreeNode(object):
    def __init__(self):
        self.children = []
        self.parent = None
        self.data = None

    def tree2list(self, prev_data=[]):
        if self.children:
            child_data = []
            for child in self.children:
                child_data.extend(child.tree2list(prev_data + [self.data]))
            return child_data
        else:
            return [prev_data + [self.data]]
