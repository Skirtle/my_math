from custom_math import *

if __name__ == "__main__":
    values = ["F", "O", "M", "T", "P", "E", "N", "H", "R", "A"]
    edges = [
        ["F", "O", "T"],
        ["F", "O", "M", "T", "P", "E"],
        ["O", "M"],
        ["F", "O", "T", "N", "H"],
        ["O", "P", "N", "H", "R", "E"],
        ["O", "E", "R", "P"],
        ["T", "P", "N", "A"],
        ["P", "H", "A", "E"],
        ["P", "E", "R", "A"],
        ["N", "H", "R", "A"]
    ]
    new_graph = Graph(value_list = values, edge_map = edges)
    print(new_graph)
    
    word = "Phantom of the Opera"
    print(word, check_for_word(new_graph, word))
        