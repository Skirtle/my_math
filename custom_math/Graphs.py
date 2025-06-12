class Vertex:
    _max_print_neighbors = 10
    _default_edge_weight = 0
    
    def __init__(self, value = None, neighbors = None, weights = None, label = None):
        self.value = value
        if (neighbors == None): self.neighbors = []
        else: self.neighbors = [x for x in neighbors]
        
        if (weights == None): self.weights = [Vertex._default_edge_weight for x in self.neighbors] # None weight for each neighbor
        else: self.weights = [x for x in weights]
        
        if (label == None): self.label = str(self.value)
        else: self.label = str(label)
        
    def add_neighbors(self, *new_vertexs) -> None:
        for vertex in new_vertexs:
            if (isinstance(vertex, Vertex)): 
                self.neighbors.append(vertex)
                self.weights.append(Vertex._default_edge_weight)
            elif (isinstance(vertex, list)): 
                self.neighbors += vertex
                self.weights += [Vertex._default_edge_weight for x in vertex]
        
            
    def add_weights(self, *new_weights) -> None:
        for weight in new_weights:
            if (isinstance(weight, Vertex)): self.weights.append(weight)
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
        return f"Vertex({self.value})"
    
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
    # Currently, only supports graphs without duplicate edges and unique labels per vertex
    # Meaning no vertex can have two ways to get to the same neighbor
    vertexs: list = None
    is_weighted: bool = False
    
    def __init__(self, value_list: list = None, edge_map: list = None, weight_map: list = None, is_weighted: bool = False, label: str = None):
        self.vertexs = _generate_graph_list(value_list, edge_map, weight_map)
        self.is_weighted = is_weighted
        self.label = "Graph" if label == None else str(label)
               
    def has_value(self, target) -> bool:
        for vertex in self.vertexs:
            if (vertex.value == target): return True
        return False
    
    def has_label(self, target) -> bool:
        for vertex in self.vertexs:
            if (vertex.label == target): return True
        return False
    
    def add_vertex(self, value, edges: list = None, weights: list = None) -> None:
        self.vertexs.append(Vertex(value = value, neighbors = edges, weights = weights))
        
    def remove_vertex_by_label(self, label) -> None:
        # Remove all references to this vertex in neighbors and weights
        for vertex in self.vertexs:
            for neighbor_index, neighbor in enumerate(vertex.neighbors):
                if (neighbor.label == label): # Vertex reference found, remove from neighbors and weights
                    vertex.neighbors.pop(neighbor_index)
                    vertex.weights.pop(neighbor_index)
                    break
        
        # Remove Vertex from vertexs
        for index, vertex in enumerate(self.vertexs):
            if (vertex.label == label): # Found vertex, remove and stop loop
                self.vertexs.pop(index)
                break
            
    def remove_vertex_by_value(self, value) -> None:
        # Remove all references to this vertex in neighbors and weights
        for vertex in self.vertexs:
            for neighbor_index, neighbor in enumerate(vertex.neighbors):
                if (neighbor.value == value): # Vertex reference found, remove from neighbors and weights
                    vertex.neighbors.pop(neighbor_index)
                    vertex.weights.pop(neighbor_index)
                    break
        
        # Remove Vertex from vertexs
        for index, vertex in enumerate(self.vertexs):
            if (vertex.value == value): # Found vertex, remove and stop loop
                self.vertexs.pop(index)
                break
    
    def get_vertex_by_value(self, target) -> Vertex:
        for vertex in self.vertexs:
            if (vertex.value == target): return vertex
        return None
    
    def get_vertex_by_label(self, target) -> Vertex:
        for vertex in self.vertexs:
            if (vertex.label == target): return vertex
        return None
          
    def __str__(self):
        s = "Label (value), neighbors: ['Neightbor label (weight)', ...]\n"
        for vertex in self.vertexs:
            s += str(vertex) + "\n"
        return s
    
    def __repr__(self):
        return f"{self.label}, {len(self.vertexs)} vertexs, {'weighted' if self.is_weighted else 'non-weighted'}"

# Private functions
# TODO: Remove this and fix _generate_graph_list() to not need it
def _get_vertex(graph, label) -> Vertex:
    for vertex in graph:
        if (vertex.label == label): return vertex
    return None

def _generate_graph_list(value_list: list = None, edge_map: list = None, weight_map: list = None) -> list:
    # TODO: Move this to Graph __init__()
    graph = []
    
    # Create base vertexs
    if (value_list != None):
        for value in value_list:
            new_vertex = Vertex(value = value, label = value)
            new_vertex.set_value(value, True)
            graph.append(new_vertex)
    
    # Add neighbors
    if (edge_map != None):
        for index, neighbor_list in enumerate(edge_map):
            graph[index].add_neighbors([_get_vertex(graph, x) for x in neighbor_list])
        
    # Add weights
    if (weight_map != None): 
        for index, weight_list in enumerate(weight_map):
            graph[index].set_weights([x for x in weight_list])
    
    
    return graph

# Public functions
def is_valid_graph_word(graph: list) -> str:
    return "".join([vertex.value for vertex in graph])

def check_for_word(graph: list, word: str) -> bool:
    # Clean the word
    cleaned_word = "".join([char.lower() for char in word if char.isalpha()])
    
    starting_vertex = None
    # Find the vertex to start from
    for vertex in graph:
        if vertex.value.lower() == cleaned_word[0]:
            starting_vertex = vertex
            break
    else: return False
    
    # Iterate through vertexs
    current_vertex = starting_vertex
    index = 1
    used_vertexs = []
    while True:
        if (index >= len(cleaned_word)): break
        
        # Found a good vertex
        for vertex in current_vertex.neighbors:
            if vertex.value.lower() == cleaned_word[index]:
                index += 1
                current_vertex = vertex
                if (vertex not in used_vertexs): used_vertexs.append(vertex)
                break
        
        else: # Went through for loop, found nothing. Failure!
            return False
    
    # Now check if the word uses all vertexs at least once
    for vertex in graph:
        if vertex not in used_vertexs: return False
    
    return True

