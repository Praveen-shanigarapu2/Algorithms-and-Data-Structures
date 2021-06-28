import  random 

class UnionbySizeDisjointSet():
    def __init__(self,n):
        self.parent = [0] * n;
        self.rank = [0] * n;
        self.sz = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1
     #TC:O(log n)       
    def find(self, x):
        while(self.parent[x] != x):
            x = self.parent[x];
        return x
    
    def display(self):
        print(self.parent)
        print(self.rank)
        
    #O(1)    
    def size(self):
        return self.sz
    
    #TC:O(log n)
    def union(self, x, y):
        idx = self.find(x)
        idy = self.find(y)
        
        if(idx == idy):
            return
            
        self.sz -=1
        
        if(self.rank[idx] > self.rank[idy]):
            self.parent[idy] = idx
            self.rank[idx] += self.rank[idy]
        else:
            self.parent[idx] = idy
            self.rank[idy] += self.rank[idx]
        
def main():
        n = 6
        s1 = UnionbySizeDisjointSet(n)
        s1.display()
        for i in range(n//2):
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
            print(x,y)
            s1.union(x,y)
            s1.display()
           # print(s1.find(0))
           # print(s1.find(n-1))
            
            
#out put
# =============================================================================
# [0, 1, 2, 3, 4, 5]
# [1, 1, 1, 1, 1, 1]
# 1 4
# [0, 4, 2, 3, 4, 5]
# [1, 1, 1, 1, 2, 1]
# 1 0
# [4, 4, 2, 3, 4, 5]
# [1, 1, 1, 1, 3, 1]
# 3 4
# [4, 4, 2, 4, 4, 5]
# [1, 1, 1, 1, 4, 1]           
# =============================================================================
            
            
            
            
            
            
            
            
            
            
if __name__ == "__main__":
        main()