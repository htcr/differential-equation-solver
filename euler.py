import numpy as np

def euler(start, end, h, f, y_start):
    # start, end: real number, 
    # the interval of target function
    # h: real number, iteration step,
    # h*(end-start) > 0
    # f: dy/dx = f(x, y) 
    # lambda expression with 2 args
    # y_start: real number, y_start
    # return: list of tuples [(x0, y0)...]

    ans = list()

    assert h*(end-start) > 0

    cur_y = y_start
    cur_x = start
    
    while cur_y <= end:
        ans.append((cur_x, cur_y))
        cur_x += h
        cur_y += h*f(cur_x, cur_y)
    
    return ans    