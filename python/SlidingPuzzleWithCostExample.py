from SearchAlgorithms.greedy_search_matrix import greedy_search
import numpy as np

class SlidingPuzzleWithHeuristic(object): 
    '''
    classdocs
    '''

    def __init__(self,num_blocks):
        '''
        Constructor
        '''
        self.num_blocks = num_blocks
        self.target=[]
                
    def __findZeroPosition(self,state):
        
        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                if state[i,j]==0:
                    row_index=i
                    col_idex=j
        return row_index,col_idex             
    
    def __numElemWrongPosition(self,state,target):
        
        wrong = 0
        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                if state[i,j]!=target[i,j]:
                    wrong=wrong+1
        return wrong
    
    def ObjectiveTest(self,current,target): 
        """Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """ 
        solution = True 
        for i in range(self.num_blocks):
            if solution == False:
                break
            for j in range(self.num_blocks):
                if current[i,j]!=target[i,j]:
                    solution = False
                    break
        return  solution
    
    def EqualityTest(self,state_a,state_b): 
        """Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """ 
        solution = True 
        for i in range(self.num_blocks):
            if solution == False:
                break
            for j in range(self.num_blocks):
                if state_a[i,j]!=state_b[i,j]:
                    solution = False
                    break
        return  solution
 
    def ExpandSolution(self,current): 
        """Returns all possible states from ``current`` 
        """ 
        
        #Inicializa o vetor com as solucoes expandidas 
        newSolutions = [] 
        
        #Para cada solucao... 
        row,column = self.__findZeroPosition(current)
                
        # Verifica quais solucoes filhas devem ser criadas. 
        # Se a linha e maior que 0 quer dizer que podemos deslocar o espaco 
        # uma casa para cima 
        if row > 0: 
            new_row=row-1
            newSolution = np.copy(current)
            TargetBlock = newSolution[new_row,column]
            newSolution[new_row,column]=0
            newSolution[row,column] = TargetBlock
            newSolutions.append(newSolution)
                
        # Se a linha e menor que num_blocks quer dizer que podemos deslocar o espaco 
        # uma casa para baixo 
        if row < self.num_blocks-1: 
            new_row=row+1
            newSolution = np.copy(current)
            TargetBlock = newSolution[new_row,column]
            newSolution[new_row,column]=0
            newSolution[row,column] = TargetBlock
            newSolutions.append(newSolution)

        # Se a coluna e maior que 0 quer dizer que podemos deslocar o espaco 
        # uma casa para esquerda 
        if column > 0: 
            new_col=column-1
            newSolution = np.copy(current)
            TargetBlock = newSolution[row,new_col]
            newSolution[row,new_col]=0
            newSolution[row,column] = TargetBlock
            newSolutions.append(newSolution)         

        # Se a coluna e menor que 3 quer dizer que podemos deslocar o espaco 
        # uma casa para direita 
        if column < self.num_blocks-1: 
            new_col=column+1
            newSolution = np.copy(current)
            TargetBlock = newSolution[row,new_col]
            newSolution[row,new_col]=0
            newSolution[row,column] = TargetBlock
            newSolutions.append(newSolution)
       
        return  newSolutions
    
    def Heuristic(self,target,current):
        
        return self.__numElemWrongPosition(current,target)

if __name__ == '__main__':
    
    #Creating a target for the game
    target=np.matrix([[1, 2, 3],[4, 5, 6],[7, 8, 0]])
    print('Target:\n%s'%target)
    
    start=np.matrix([[4, 6, 3],[1, 0, 8],[7, 2, 5]])
#    start=np.matrix([[1, 2, 3],[4, 5, 6],[7, 0, 8]])
    print('Start:\n%s'%start)
        
    #Creating an problem object based on FindPath class
    Problema = SlidingPuzzleWithHeuristic(3)
     
    #Creating an object for breadth first search algorithm for ``FindPath`` problem
    SearchObj = greedy_search(Problema)    
     
     
    #Finding solution
    solution,visited = SearchObj.search(start,target)
    if solution:
        print('Solution found!')
        print('Path:\n')
        for state in visited:
            print('%s\n'%state) 
    else:
        print('Solution not found!')        
