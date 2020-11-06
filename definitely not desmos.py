import math
import random

def relation(x, y): # relation
    #return math.sqrt(x**2 + y**2)/15
    #return x**10 + y**10 == 10**10
    #return math.sin(x)**2 + math.cos(x)**2
    return math.sin(x/5) + math.cos(y/5)
    #return (x**3 + y**3 + 100*x*y)**2 / 10000000
    
def func(x): # function
    return random.randint(-10, 10)
    #return math.e**(-(x**2/1000)) * 50
    #return math.log(x)*15
    #return 10*math.tan(x/10)
    #return 90/(math.e**-(x/20) + 1)
    #return 90*math.sin(x/10)
    #return x**3/1000
    #return (x/20)**(x/20) * 20-100

def graph(f, filename, X_RANGE=100, Y_RANGE=100, LINE_WIDTH=1, SHOW_AXIS=True, SHADED=False):
    out = open(filename, "wb")
    def pprint(val="\n"):
        out.write(val.encode())
        
    pprint(" ")
    [pprint(" ▲"[x == 0 and SHOW_AXIS]) for x in range(X_RANGE, -X_RANGE-1, -1)]
    pprint()
    
    for y in range(-Y_RANGE, Y_RANGE, 2):
        pprint(" ◄"[y == 0 and SHOW_AXIS])
        
        for x in range(X_RANGE, -X_RANGE-1, -1):
            if SHOW_AXIS and y == 0 and x == 0:
                pprint("█")
            elif SHOW_AXIS and y == 0:
                pprint("■")
            elif SHOW_AXIS and x == 0:
                pprint("█")
            else:
                try:
                    if SHADED:
                        pprint(" .:°+RÆ▒▓"[min(abs(round(f(x, y))), 8)])
                    else:
                        pprint(" ▒"[bool(f(x, y))])
                        
                except TypeError: # f takes 1 arg not 2
                    def fprime(x): #first principles
                        eps = 1e-9
                        return (f(x+eps)-f(x)) / eps
                    def a(x):
                        #a\left(t\right)=\frac{f'\left(t\right)}{\sqrt{f'\left(t\right)^{2}+1}}
                        return fprime(x)/math.sqrt(fprime(x)**2+1) #lmao
                    def b(x, w):
                        #f\left(x-ba\left(x\right)\right)-b\frac{a\left(x+a\left(x\right)\right)}{f'\left(x+a\left(x\right)\right)}\ \le\ y\le f\left(x+ba\left(x\right)\right)+b\frac{a\left(x+a\left(x\right)\right)}{f'\left(x+a\left(x\right)\right)}
                        if fprime(x+a(x)) == 0:
                            return f(x) + w
                        return f(x + w*a(x))+w*a(x+a(x))/(fprime(x+a(x))) #trust the process
                    
                    try:
                        pprint(" #"[b(-x, -LINE_WIDTH) <= -y <= b(-x, LINE_WIDTH)])
                    except: # domain error or smth, function not avaliable
                        pprint(" ")
                        
        pprint(" ►"[y == 0 and SHOW_AXIS])
        pprint()
        
    pprint(" ")
    [pprint(" ▼"[x == 0 and SHOW_AXIS]) for x in range(X_RANGE, -X_RANGE-1, -1)]
    pprint()
    out.close()

graph(relation, "output.txt", SHADED=1)
