import grapg_utils as utils
from queue import Queue

def auxDfs(u, parent, visit, inp):
    visit[u] = 1
    for v in range(len(inp)):
        if(inp[u][v]==1):
            if(visit[v]==0): #forward edge
                visit[v] = 1
                if(auxDfs(v, u, visit, inp)):
                    return True
            else: #back edge
                if(v != parent):
                    return True
    return False
                    
#TC:Theta(V^2)   SC:Theta(V)    
def detectCycle1(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(auxDfs(u, u, visit, inp)):
                return True
    return False
#================================================================
def auxBfs(u, visit, inp):
    q = Queue()
    q.put(u)
    visit[u] = 1   #in the queue
    
    while(not q.empty()):
        u = q.get()
        visit[u] = 2 #taking out of the queue
        for v in range(len(inp)):
           if(inp[u][v] == 1):
               if(visit[v] == 0):  #not Visited 
                   q.put(v)
                   visit[v] = 1
               else:
                   if(visit[v] == 1): #Visited 
                      return True
    return False
    
def detectCycle2(inp):
    n = len(inp)
    visit = [0] * n
    for u in range(n):
        if(visit[u] == 0):
            if(auxBfs(u, visit, inp)):
                return True
    return False

           
def main():
   # n = int(sys.argv[1])
    n = 4
   # inp = utils.randomUndirectedGraph(n)
# =============================================================================
# [
# [0, 1, 0, 0], 
# [1, 0, 1, 0],
# [0, 1, 0, 0], 
# [0, 0, 0, 0]
# ]
#=============================================================================
   # special case cycle exists
    #inp = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
   # inp = [[0, 1],[1, 0]]
    inp = utils.randomUndirectedGraph(n)

   # utils.display(inp)
    print(detectCycle1(inp))
    print(detectCycle2(inp))
    #print(detectCycle3(inp))
    
if __name__=="__main__":
    main()

            