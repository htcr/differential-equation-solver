import numpy as np

def euler(start, end, h, f, y_start):
    # start, end: real number, 
    # the interval of target function
    # h: real number, iteration step,
    # h*(end-start) > 0
    # f: dy/dx = f(x, y)
    # y_start: real number, y_start
    ans = list()
    
    