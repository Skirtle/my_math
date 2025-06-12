class Node:
    _max_print_neighbors = 10
    _default_edge_weight = 0
    
    def __init__(self, value = None, neighbors = None, weights = None, label = None):
        self.value = value
        if (neighbors == None): self.neighbors = []
        else: self.neighbors = [x for x in neighbors]
        
        if (weights == None): self.weights = [Node._default_edge_weight for x in self.neighbors] # None weight for each neighbor
        else: self.weights = [x for x in weights]
        
        if (label == None): self.label = str(self.value)
        else: self.label = str(label)
        
    def add_neighbors(self, *new_nodes) -> None:
        for node in new_nodes:
            if (isinstance(node, Node)): 
                self.neighbors.append(node)
                self.weights.append(Node._default_edge_weight)
            elif (isinstance(node, list)): 
                self.neighbors += node
                self.weights += [Node._default_edge_weight for x in node]
        
            
    def add_weights(self, *new_weights) -> None:
        for weight in new_weights:
            if (isinstance(weight, Node)): self.weights.append(weight)
            elif (isinstance(weight, list)): self.weights += weight
            
    def __str__(self) -> str:
        s = f"{self.label} ({self.value}), neighbors: "
        if (len(self.neighbors)) >= self._max_print_neighbors:
            neighbor_str = f"[{len(self.neighbors)} other neighrbors]"
        
        else: 
            neighbor_list = [x.label for x in self.neighbors]
            weight_list = [x for x in self.weights]
            
            
            if (len(neighbor_list) != len(weight_list)): 
                exit(f"Neighbors and Weights must be the same length. Got {len(neighbor_list):} and {len(weight_list):}")
            
            f = [f"{neighbor_list[i]} ({weight_list[i]})" for i in range(len(neighbor_list))]
            neighbor_str = str(f)
        return s + neighbor_str
            
    def __repr__(self) -> str:
        return f"Node({self.value})"
    
    def set_value(self, value, set_value_as_label: bool = False) -> None: 
        self.value = value
        if (set_value_as_label): self.set_label(self.value)
    
    def set_label(self, label: str) -> None:
        self.label = label
    
    def set_weights(self, weights: list) -> None:
        if (len(weights) != len(self.neighbors)):
            # TODO: Error here
            ...
        self.weights = [x for x in weights] # Copy values, not the list itself
    
    def get_label(self) -> str:
        return self.label
    
    def get_value(self): 
        return self.value
    
    def get_weights(self) -> list:
        return self.weights

class Graph:
    # Currently, only supports graphs without duplicate edges and unique labels per node
    # Meaning no node can have two ways to get to the same neighbor
    nodes: list = None
    is_weighted: bool = False
    
    def __init__(self, value_list: list = None, edge_map: list = None, weight_map: list = None, is_weighted: bool = False, label: str = None):
        self.nodes = _generate_graph_list(value_list, edge_map, weight_map)
        self.is_weighted = is_weighted
        self.label = "Graph" if label == None else str(label)
               
    def has_value(self, target) -> bool:
        for node in self.nodes:
            if (node.value == target): return True
        return False
    
    def has_label(self, target) -> bool:
        for node in self.nodes:
            if (node.label == target): return True
        return False
    
    def add_node(self, value, edges: list = None, weights: list = None) -> None:
        self.nodes.append(Node(value = value, neighbors = edges, weights = weights))
        
    def remove_node_by_label(self, label) -> None:
        # Remove all references to this node in neighbors and weights
        for node in self.nodes:
            for neighbor_index, neighbor in enumerate(node.neighbors):
                if (neighbor.label == label): # Node reference found, remove from neighbors and weights
                    node.neighbors.pop(neighbor_index)
                    node.weights.pop(neighbor_index)
                    break
        
        # Remove Node from nodes
        for index, node in enumerate(self.nodes):
            if (node.label == label): # Found node, remove and stop loop
                self.nodes.pop(index)
                break
            
    def remove_node_by_value(self, value) -> None:
        # Remove all references to this node in neighbors and weights
        for node in self.nodes:
            for neighbor_index, neighbor in enumerate(node.neighbors):
                if (neighbor.value == value): # Node reference found, remove from neighbors and weights
                    node.neighbors.pop(neighbor_index)
                    node.weights.pop(neighbor_index)
                    break
        
        # Remove Node from nodes
        for index, node in enumerate(self.nodes):
            if (node.value == value): # Found node, remove and stop loop
                self.nodes.pop(index)
                break
    
    def get_node_by_value(self, target) -> Node:
        for node in self.nodes:
            if (node.value == target): return node
        return None
    
    def get_node_by_label(self, target) -> Node:
        for node in self.nodes:
            if (node.label == target): return node
        return None
          
    def __str__(self):
        s = "Label (value), neighbors: ['Neightbor label (weight)', ...]\n"
        for node in self.nodes:
            s += str(node) + "\n"
        return s
    
    def __repr__(self):
        return f"{self.label}, {len(self.nodes)} nodes, {'weighted' if self.is_weighted else 'non-weighted'}"

# Private functions
# TODO: Remove this and fix _generate_graph_list() to not need it
def _get_node(graph, label) -> Node:
    for node in graph:
        if (node.label == label): return node
    return None

def _generate_graph_list(value_list: list = None, edge_map: list = None, weight_map: list = None) -> list:
    # TODO: Move this to Graph __init__()
    graph = []
    
    # Create base nodes
    if (value_list != None):
        for value in value_list:
            new_node = Node(value = value, label = value)
            new_node.set_value(value, True)
            graph.append(new_node)
    
    # Add neighbors
    if (edge_map != None):
        for index, neighbor_list in enumerate(edge_map):
            graph[index].add_neighbors([_get_node(graph, x) for x in neighbor_list])
        
    # Add weights
    if (weight_map != None): 
        for index, weight_list in enumerate(weight_map):
            graph[index].set_weights([x for x in weight_list])
    
    
    return graph

def is_valid_graph_word(graph: list) -> str:
    return "".join([node.value for node in graph])

def check_for_word(graph: list, word: str) -> bool:
    # Clean the word
    cleaned_word = "".join([char.lower() for char in word if char.isalpha()])
    
    starting_node = None
    # Find the node to start from
    for node in graph:
        if node.value.lower() == cleaned_word[0]:
            starting_node = node
            break
    else: return False
    
    # Iterate through nodes
    current_node = starting_node
    index = 1
    used_nodes = []
    while True:
        if (index >= len(cleaned_word)): break
        
        # Found a good node
        for node in current_node.neighbors:
            if node.value.lower() == cleaned_word[index]:
                index += 1
                current_node = node
                if (node not in used_nodes): used_nodes.append(node)
                break
        
        else: # Went through for loop, found nothing. Failure!
            return False
    
    # Now check if the word uses all nodes at least once
    for node in graph:
        if node not in used_nodes: return False
    
    return True