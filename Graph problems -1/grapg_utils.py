import  random
def randomUndirectedGraph(n):
    inp =[ [0] * n for i in range(n)]
    for i in range(n):
        u = random.randint(0,n-1)
        v = random.randint(0,n-1)
        if(u != v):
            inp[u][v] = 1
            inp[v][u] = 1
    print(inp)
    return inp
    