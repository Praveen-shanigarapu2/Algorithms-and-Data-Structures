import grapg_utils as utils
from queue import  Queue

def auxDfs(u, visit, inp):
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v] == 1 and visit[v] == 0):
            auxDfs(v,visit, inp)

def countCircles1(inp):
    n = len(inp)
    ncircles = 0
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            auxDfs(u, visit, inp)
            ncircles += 1
    print(ncircles)
#-----------------------------------------    
def auxBfs(u, visit, inp):
    q = Queue()
    q.put(u)
    while(not q.empty()):
        u = q.get()
        for v in range(len(inp)):
            if(inp[u][v] == 1 and visit[v] == 0):
                q.put(v)
                visit[v]= 1
    
def countCircles2(inp):
    n = len(inp)
    ncircles = 0
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            auxBfs(u,visit,inp)
            ncircles += 1
    print(ncircles)
        
    
    
    
    
    
def main():
    print("Test")
    inp = utils.randomUndirectedGraph(4)
    countCircles1(inp)
    countCircles2(inp)

if __name__=="__main__":
    main()