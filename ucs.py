import copy
import queue as Q

class Graph:
    def __init__(self):
        self.graph = dict()
        self.cost_dict=dict()
        self.final_dict=dict()


    def addEdge(self,u,v,c):
    
        if u not in self.graph:
            qu = Q.PriorityQueue()
            self.graph.update({u:qu})

        self.graph[u].put(v)
        self.cost_dict.update({(u,v):c})
    

    def UCS_util(self,s,visited,path,goal,value):
    
        path.append(s)
    
        visited[s]=True
    
    
        if goal==s:
            self.final_dict.update({tuple(path):value})
            return
    
   
        for i in self.graph[s].queue:
            if visited[i]==False:
            
                self.UCS_util(i,copy.deepcopy(visited),copy.deepcopy(path),goal,value + self.cost_dict[s,i])

    def UCS(self, s,goal):
        self.visited = [False]*20
        self.visited[s] = True
        path=[s]
    
        for i in self.graph[s].queue:
            if self.visited[i] == False:
                value = self.cost_dict[s,i]
                self.UCS_util(i,copy.deepcopy(self.visited),copy.deepcopy(path),goal,value)

        if bool(self.final_dict):
            return min(self.final_dict, key=self.final_dict.get)
        return None
   


   
        
            
        
g = Graph()
# Dua vao so nut tren ban do


f = open("input.txt", "r")
for line in f:
    u, v ,w= [int(it) for it in line.strip().split(' ')]
    g.addEdge(u,v,w)
f.close()

with open('output.txt', 'wt') as gp:
    tmp =g.UCS(0,5)
    gp.write(' '.join([str(it) for it in tmp]))
# g.addEdge(0,1,5)
# g.addEdge(1,2,3)
# g.addEdge(2,3,10)
# g.addEdge(3,4,6)
# g.addEdge(1,4,5)
# g.addEdge(4,5,8)
# g.addEdge(0,5,20)

#source code: https://github.com/samsil2/Algorithm/blob/master/ucs.py


