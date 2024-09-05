class Node:
    def __init__(self, parent, currentPosition, stateMatrix, goalPosition):
        self.currentPosition = currentPosition  # (y,x)
        self.stateMatrix = stateMatrix
        self.goalPosition = goalPosition  # (y,x)
        self.parent = parent

    def isGoal(self) -> bool:
        return self.currentPosition == self.goalPosition

    def expand(self) -> list:
        # vamos a generar los children
        rowLen = len(self.stateMatrix) - 1
        columLen = len(self.stateMatrix[0]) - 1
        children = []

        # izquierda
        y1 = self.currentPosition[0] 
        x1 = self.currentPosition[1] - 1
        
        if x1 >= 0  and self.stateMatrix[y1][x1] != '1':
            children.append(
                Node(self, (y1, x1), self.stateMatrix.copy(), self.goalPosition)
            )

        # derecha
        y1 = self.currentPosition[0] 
        x1 = self.currentPosition[1] + 1
        
        if  x1 <= columLen and self.stateMatrix[y1][x1] != '1':
            children.append(
                Node(self, (y1, x1), self.stateMatrix.copy(), self.goalPosition)
            )
        # arriba
       
        y1 = self.currentPosition[0] - 1
        x1 = self.currentPosition[1]
        
        if y1 >= 0 and self.stateMatrix[y1][x1] != '1':
            children.append(
                Node(self, (y1, x1), self.stateMatrix.copy(), self.goalPosition)
            )
        
        # abajo
        y1 = self.currentPosition[0] + 1
        x1 = self.currentPosition[1]
        
 
        if  y1 <= rowLen  and self.stateMatrix[y1][x1] != '1':
            children.append(
                Node(self, (y1, x1), self.stateMatrix.copy(), self.goalPosition)
            )

        return children
