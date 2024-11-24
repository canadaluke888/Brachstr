class Tree:
    def __init__(self):
        """
        Initialize the tree with an empty root node.
        """
        self.tree = {}

    def add_node(self, parent, node):
        """
        Add a node to the tree.
        :param parent: The paraent node under which the new node will be added.
        :param node: The new node to add.
        """
        if parent is None:
            # If no parent is specified, add to root.
            if node not in self.tree:
                self.tree[node] = {}
        else:
            # Recursively find the parent and add the new node.
            self._add_node_recursive(self.tree, parent, node)

    def _add_node_recursive(self, current_tree, parent, node):
        """
        Recursively find the parent node and add the new node.
        :param currrent_tree: The currrent subtree being searched.
        :param parent: The parent node to search for.
        :param node: The new node to add.
        """
        if parent in current_tree:
            # Add the node if the parent is found.
            if node not in current_tree[parent]:
                current_tree[parent][node] = {}
        else:
            # Search in each child node recursively.
            for child in current_tree:
                self._add_node_recursive(current_tree[child], parent, node)

    def get_tree(self):
        """
        Get the entire tree structure.
        :return: The tree as a nested dictionary.
        """
        return self.tree
    
    def print_tree(self):
        """
        Print the tree structure for debugging purposeses.
        """
        import pprint
        pprint.pprint(self.tree)