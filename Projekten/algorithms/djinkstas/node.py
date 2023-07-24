# from itertools import permutations
import numpy as np
import pandas as pd
from sys import path

class node:
    def __init__(self, value, name):
        self.value = value
        self.name = name
        self.linked_nodes = []
    def __repr__(self) -> str:
        return f"name: {self.name}"
    def link(self, different_node, linkage_value):
        self.linked_nodes.append([different_node, linkage_value])
    def show_linked(self):
        return self.linked_nodes
    
def get_data():
    global node
    df = pd.read_csv(f"{path[0]}/node_df.csv")
    list_of_nodes = []

    nodes = np.union1d(np.array(df["Source"]), np.array(df["Target"]))
    for node_name in nodes:
        list_of_nodes.append(node(np.inf, node_name))
    for selected_node in list_of_nodes:
        print(selected_node.name)
get_data()