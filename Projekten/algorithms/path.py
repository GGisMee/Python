from itertools import permutations
import numpy as np
class link():
    def one_to_more(node, node_list, linkage_value_list, link_both_ways=False):
        if not (isinstance(node_list, list) or isinstance(node_list, np.ndarray)): # möjlighet att inte använda enkelvärden
            node1.link(node_list, linkage_value_list)
            return
            node_list.link(node1, linkage_value)
        for i,other_node in enumerate(node_list):
            node.link(other_node, linkage_value_list[i])
            if link_both_ways:
                other_node.link(node, linkage_value_list[i])
    def two(node1, node2, linkage_value):
        node1.link(node2, linkage_value)
        node2.link(node1, linkage_value)
    
    def one(from_node, to_node, linkage_value): # from_node kommer att veta vilken den är linkad med, men ej den andra
        from_node.link(to_node, linkage_value)

class node:
    def __init__(self, value):
        self.value = value
        self.linked_nodes = []
    def link(self, different_node, linkage_value):
        self.linked_nodes.append([different_node, linkage_value])
    def show_linked(self):
        return self.linked_nodes

node1 = node(0)
node2 = node(1)
node3 = node(2)
link.one_to_more(node1, [node2, node3], [3,6])

print(node1.linked_nodes)
