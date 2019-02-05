# Euler 255
# Kelvin Blaser
# 2019.02.05
#
#  I bet there will be long stretches of consecutive integers where the number 
#  of iterations remains constant
#
#  Not the most efficient.  Takes a few minutes to run.

import matplotlib.pyplot as plt

def sqrRootIterate(n, x):
    # Ceiling divide
    y = n//x
    if y*x < n:
        y += 1
    # Floor divide
    return (x+y)//2
    
def sqrRootIterations(n):
    d = len(str(n))
    if d % 2 == 0:
        x = 7*pow(10, (d-2)//2)
    else:
        x = 2*pow(10, (d-1)//2)
    
    last = -1
    iters = 0
    while x != last:
        last = x
        x = sqrRootIterate(n, x)
        iters += 1
    return x, iters
    
def averageIterations(lo, hi, talk=False):
    rMin = sqrRootIterations(lo)[0] + 1
    rMax = sqrRootIterations(hi)[0] - 1
    
    totalIterations = 0
    for r in range(rMin, rMax+1):
        if talk and r%(10**4) == 0:
            print '{0} <= {1} <= {2}'.format(rMin, r, rMax)
        f = float(r)
        rbot = int((f-0.5)**2)+1
        rtop = int((f+0.5)**2)
        while rbot < rtop:
            bot = rbot
            top = rtop+1
            i = sqrRootIterations(rbot)[1]
            while top > bot:
                mid = bot + (top - bot) // 2
                iterMid = sqrRootIterations(mid)[1]
                if iterMid > i:
                    top = mid
                else:
                    bot = mid + 1
            #print r, i, rbot, bot, rtop
            totalIterations += i*(bot - rbot)
            rbot = bot
            
    for x in range(lo, int((float(rMin)-0.5)**2) + 1):
        totalIterations += sqrRootIterations(x)[1]
    #print lo, x, int((float(rMax)+0.5)**2) + 1, hi
    for x in range(int((float(rMax)+0.5)**2) + 1, hi+1):
        totalIterations += sqrRootIterations(x)[1]
        
    return float(totalIterations) / (hi-lo+1)
        
    
if __name__ == '__main__':
    print 'Square Root of 4321'
    print 'sqrRootIterate({0},{1}) = {2}'.format(4321, 70, sqrRootIterate(4321, 70))
    print 'sqrRootIterate({0},{1}) = {2}'.format(4321, 66, sqrRootIterate(4321, 66))
    print 'sqrt({0}) = {1}, calculated in {2} iterations'.format(4321, *sqrRootIterations(4321))
    print ''
    print ' Slow Method - 5 digit numbers'
    iters = [sqrRootIterations(n) for n in range(10000, 100000)]
    
    #fig = plt.figure('Euler 255')
    f = plt.figure(num='slow')
    f.clf()
    fig, ax1 = plt.subplots(num='slow')
    color = 'b'
    ax1.set_xlabel('n')
    ax1.set_ylabel('Iterations', color=color)
    ax1.plot(range(10000,100000), [i[1] for i in iters], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax2 = ax1.twinx()
    color = 'r'
    ax2.set_ylabel('Sqrt(n)', color=color)
    ax2.plot(range(10000,100000), [i[0] for i in iters], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    plt.show()
    
    totalIters = sum(i[1] for i in iters)
    print 'Average iterations : {0:.10f}'.format(float(totalIters) / 90000)
    
    print ''
    print ' Fast Method - 5 digit numbers'
    print 'Average iterations : {0:.10f}'.format(averageIterations(10000, 99999))
    
    print ''
    print ' Fast method - 14 digit numbers'
    print 'Average iterations : {0:.10f}'.format(averageIterations(10**13, 10**14 - 1, True))