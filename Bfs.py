from Node import Node
from os import system
class Bfs:
    def __init__(self) -> None:
        pass
    
   
    def loadMatrix(self,matrixName):
        self.initMatrix = []
        self.initPosition = None
        self.goalPosition = None
        
        with open(matrixName + '.txt', "+r") as file:
            rows = file.readlines()
            for i in range(len(rows)):
                row = []
                for j in range(len(rows[i].strip())):
                    if self.initPosition is None and rows[i][j] == "*":
                        self.initPosition = (i, j)
                    if self.goalPosition is None and rows[i][j] == "Q":
                        self.goalPosition = (i, j)
                    row.append(rows[i][j])
                
                self.initMatrix.append(row)
        print(self.initPosition)    
            
    def run(self):
        
        initNode = Node(None,self.initPosition,self.initMatrix,self.goalPosition)
        
        queue = [initNode]
        nodesVisited = []
        
        while len(queue) != 0:
            
            currentNode:Node = queue.pop(0)
            
            if(currentNode.isGoal()):
                return currentNode          
             
            childs:list =  currentNode.expand()
                 
            nodesVisited.append(currentNode.currentPosition)
            
            for child in childs:
                if child.currentPosition not in nodesVisited:
                    queue.append(child)
                    
                
            
        raise ValueError('No existe solicion')  

    
    
    

bfs =  Bfs()
bfs.loadMatrix('matriz2')

goalNode = bfs.run()
print(goalNode.currentPosition)

