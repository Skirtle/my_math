from custom_math import *

if __name__ == "__main__":
    char_f = Vertex("F"); char_o = Vertex("O"); char_m = Vertex("M"); char_t = Vertex("T")
    char_p = Vertex("P"); char_e = Vertex("E"); char_n = Vertex("N")
    char_h = Vertex("H"); char_r = Vertex("R"); char_a = Vertex("A")
    
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
    # new_graph = _generate_graph_list([1, 2, 3, 4, 5], [[5, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1]])
    
    g = Graph([1, 2, 3, 4, 5], [[5, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 1]])
    
    print(g)
    print(g)
        