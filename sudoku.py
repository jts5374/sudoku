class Sudoku:
    def __init__(self, grid) -> None:
        self.setgrid(grid)
        self.counter = 0
        self.CHOICES ={1,2,3,4,5,6,7,8,9}
    def __repr__(self):
        output = ''
        for row in self.grid:
            output += ' '.join([str(r) for r in row]) + '\n'

        return output
    def setgrid(self, s):
        self.grid = self.generategrid(s)

    def generategrid(self, str):
        grid = []
        for i in range(0, 81, 9):
            grid += [[int(char) for char in str[i:i+9]]]

        return grid

    def possible(self, x, y, val):
        row = [self.grid[x][j] for j in range(9)]
        col = [self.grid[i][y] for i in range(9)]

        x0 = (x//3)*3
        y0 = (y//3)*3

        cell = [self.grid[x0+i][y0+j] for i in range(0,3) for j in range(0,3)]

        if val in row or val in col or val in cell:
            return False
        
        return True
    
    

    def solve(self):
        for i in range(9):
            for j in range(9):
                self.counter+=1               
                if self.grid[i][j] == 0:    
                    for x in range(1,10):                         
                        if self.possible(i,j,x):                   
                            self.grid[i][j] = x
                            self.solve()
                            self.grid[i][j]=0
            
                    return
        print(self, f'It took {self.counter} steps to arrive at this answer', sep='\n')

x = Sudoku("080070305257008096000005070409360000061000040378010020030001904705000182006482500")
# hardest sudoku "800000000003600000070090200050007000000045700000100030001000068008500010090000400"

x.solve()
