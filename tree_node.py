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

    def get_length_to_root(self):
        length_to_root = 0
        tmp = self
        while tmp.parent is not None:
            length_to_root = length_to_root + 1
            tmp = tmp.parent
        return length_to_root

    def get_data_list_from_root(self):
        data_list = []
        data_list.insert(0, self.data)
        tmp = self
        while tmp.parent is not None:
            tmp = tmp.parent
            data_list.insert(0, tmp.data)
        return data_list
