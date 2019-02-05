import numpy as np
import matplotlib.pyplot as plt

def updateGrid(grid, ant_x, ant_y, ant_dir):
    # Rotate Direction
    if grid[ant_x, ant_y]:
        ant_dir += 1
    else:
        ant_dir += 3
    ant_dir %= 4
    
    # Update Grid
    grid[ant_x, ant_y] = ~grid[ant_x, ant_y]
    
    # Move  ant
    if ant_dir == 0:
        ant_x += 1
    if ant_dir == 1:
        ant_y += 1
    if ant_dir == 2:
        ant_x -= 1
    if ant_dir == 3:
        ant_y -= 1
    
    return ant_x, ant_y, ant_dir
    

def Euler349(N):
    grid = np.zeros((500,500), dtype=np.bool_)
    ant_x, ant_y, ant_dir = 250, 250, 0
    blackSquares = [0]*min(11001, N+1)
    for ix in range(min(N, 11000)):
        if grid[ant_x, ant_y]:
            blackSquares[ix+1] = blackSquares[ix] - 1
        else:
            blackSquares[ix+1] = blackSquares[ix] + 1
        ant_x, ant_y, ant_dir = updateGrid(grid, ant_x, ant_y, ant_dir)
    plt.imshow(grid) 
    plt.show()
    if N <= 11000:
        return blackSquares[N]
    period = 104
    diff = blackSquares[11000] - blackSquares[11000 - period]
    return blackSquares[10500 + (N-10500)%104] + diff*((N-10500)//period)
    
if __name__ == '__main__':
    print Euler349(2000)
    print Euler349(10**18)