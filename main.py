from custom_math import *

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
    new_graph = generate_graph([1, 2, 3, 4, 5], [[5, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1]])
    
    print(new_graph)
    for node in new_graph:
        print(node)
        