# Euler 393 - Migrating Ants
# projecteuler.net/problem=393
#
# Kelvin Blaser 2014.02.26

import scipy as sp

U = 0
D = 1
L = 2
R = 3
T = 4

def possible_dirs(board, head, tail):
    dirs = []
    Nx, Ny = board.shape
    x,y = head
    if x > 0 and board[x-1, y]:
        dirs.append(U)  # Up
    if x < Nx-1 and board[x+1, y]:
        dirs.append(D)  # Down
    if y > 0 and board[x, y-1]:
        dirs.append(L)
    if y < Ny-1 and board[x, y+1]:
        dirs.append(R)
    if tail == (x+1,y) or tail == (x-1, y) or tail == (x, y-1) or tail == (x, y+1):
        dirs.append(T)
    return dirs
    
def move(board, head, tail, d):
    x,y = head
    if d == U:
        board[x-1, y] = False
        head = (x-1, y)
    if d == D:
        board[x+1, y] = False
        head = (x+1, y)
    if d == L:
        board[x, y-1] = False
        head = (x, y-1)
    if d == R:
        board[x, y+1] = False
        head = (x, y+1)
    if d == T:
        head = tail
    return head, tail
    
def next_board(board, memo):
    #print 'In next_board'
    #print board
    if not any([any(x) for x in board]):
     #   print 'I returned 1'
        return 1
    Nx, Ny = board.shape
    xc = 0
    yc = 0
    xl = 0
    yl = 0
    xh = Nx-1
    yh = Ny-1
    while not any(board[xc,:]):
        xc += 1
        xl += 1
    while not board[xc,yc]:
        yc += 1
    while not any(board[:,yl]):
        yl += 1
    while not any(board[xh,:]):
        xh -= 1
    while not any(board[:,yh]):
        yh -= 1
    if xc == Nx-1 or yc == Ny-1:
    #    print 'I returned 0 (Size)'
        return 0
    new_board = sp.copy(board[:,:])
    new_board[xc,yc] = False
    if not (new_board[xc+1,yc] and new_board[xc,yc+1]):
     #   print 'I returned 0 (Room)'
        return 0
    new_board[xc+1,yc] = new_board[xc,yc+1] = False
    new_board = sp.copy(new_board[xl:xh+1, yl:yh+1])
    return 2 * count_ways(new_board, (xc+1 - xl,yc-yl), (xc-xl,yc+1-yl), memo)
    
def count_ways(board, head, tail, memo={}):
    #print board
    #print head
    #print tail
    #raw_input('Enter Something: ')
    key = tuple([tuple(x) for x in board]+[head,tail])
    #if key in memo:
    #    return memo[key]
    dirs = possible_dirs(board, head, tail)
    if not dirs:
        return 0
    ways = 0
    for d in dirs:
        new_board = sp.copy(board)
        new_head, new_tail = move(new_board, head, tail, d)
        if new_head == new_tail:
            ways += next_board(new_board, memo)
            continue
        t_dirs = possible_dirs(new_board, new_tail, new_head)
        h_dirs = possible_dirs(new_board, new_head, new_tail)
        cont = False
        while len(t_dirs) == 1 or len(h_dirs) == 1:
            if len(t_dirs) == 1:
                d = t_dirs[0]
                new_tail, new_head = move(new_board, new_tail, new_head, d)
                if new_head == new_tail:
                    ways += next_board(new_board, memo)
                    cont = True
                    break
            h_dirs = possible_dirs(new_board, new_head, new_tail)
            if len(h_dirs) == 1:
                d = h_dirs[0]
                new_head, new_tail = move(new_board, new_head, new_tail, d)
                if new_head == new_tail:
                    ways += next_board(new_board, memo)
                    cont = True
                    break
            t_dirs = possible_dirs(new_board, new_tail, new_head)
            h_dirs = possible_dirs(new_board, new_head, new_tail)
        if cont:
            continue
        ways += count_ways(new_board, new_head, new_tail, memo)
    #print ways
    #memo[key] = ways
    return ways
    
def Euler393(N=4):
    board = sp.ones((N,N),dtype=bool)
    board[0,0] = False
    board[0,1] = False
    board[1,0] = False
    head = (1,0)
    tail = (0,1)
    return 2*count_ways(board, head, tail)
     