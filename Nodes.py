class Node:
    # This allows for directional and bidirectional graphs
    # Weighted graph will be in another Node class later on, probably WeightedNode
    _max_print_neighbors = 10
    
    def __init__(self, val = None, nodes = None):
        self.value = val
        if (nodes == None): self.neighbors = []
        else: self.neighbors = [x for x in nodes]
        
    def add_neighbors(self, *new_nodes):
        for node in new_nodes:
            if (isinstance(node, Node)): self.neighbors.append(node)
            elif (isinstance(node, List)): self.neighbors += node
            
    def __str__(self):
        s = f"{self.value}, neighbors: "
        if (len(self.neighbors)) >= self._max_print_neighbors:
            neighbor_str = f"[{len(self.neighbors)} other neighrbors]"
        else: 
            neighbor_str = f"{[x.value for x in self.neighbors]}"
        return s + neighbor_str
            
    def __repr__(self):
        return f"Node({self.value})"

def get_graph_values(graph) -> list:
    return [node.value for node in graph]

def graph_to_str(graph) -> str:
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

if __name__ == "__main__":
    char_f = Node("F"); char_o = Node("O"); char_m = Node("M"); char_t = Node("T")
    char_p = Node("P"); char_e = Node("E"); char_n = Node("N")
    char_h = Node("H"); char_r = Node("R"); char_a = Node("A")
    
    char_f.add_neighbors(char_f, char_o, char_t)
    char_o.add_neighbors(char_f, char_o, char_m, char_t, char_p, char_e)
    char_m.add_neighbors(char_o, char_m)
    char_t.add_neighbors(char_f, char_o, char_t, char_n, char_h)
    char_p.add_neighbors(char_o, char_p, char_n, char_h, char_r, char_e)
    char_e.add_neighbors(char_o, char_e, char_r, char_p)
    char_n.add_neighbors(char_t, char_p, char_n, char_a)
    char_h.add_neighbors(char_p, char_h, char_a, char_e)
    char_r.add_neighbors(char_p, char_e, char_r, char_a)
    char_a.add_neighbors(char_n, char_h, char_r, char_a)
    
    graph = [char_f, char_o, char_m, char_t, char_p, char_e, char_n, char_h, char_r, char_a]
    
    
    print(check_for_word(graph, "Phantom of the Opera"))
    