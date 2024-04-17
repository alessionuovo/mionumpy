import numpy as np
def arit_progress(num, add, rows, cols):
    x=[]
    sum=num
    for i in range(rows):
        y=[]
        for j in range(cols):
            y.append(sum)
            sum+=add
        x.append(y)
    return np.matrix(x)    
def geom_progress(num, mult, rows, cols):
    x=[]
    multi=num
    for i in range(rows):
        y=[]
        for j in range(cols):
            y.append(multi)
            multi*=mult
        x.append(y)
    return np.matrix(x) 
def pow(num,  rows, cols):
    x=[]
    res=num
    for i in range(rows):
        y=[]
        for j in range(cols):
            y.append(res)
            res*=num
        x.append(y)
    return np.matrix(x)    
    