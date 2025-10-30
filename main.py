import custom_math as c_math



if __name__ == "__main__":
    ll = c_math.LinkedList()
    
    for i in range(5):
        ll.append(i * 2)
    
    for i in range(5):
        print(f"{i = }, {ll.index(i * 2) = }")