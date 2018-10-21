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
    
    iter_num = int((end-start)/h)

    for i in range(iter_num):
        ans.append((cur_x, cur_y))
        cur_y += h*f(cur_x, cur_y)
        cur_x += h

    ans.append((cur_x, cur_y))
    
    return ans    

fxy = lambda x, y: 1.0 / 3*(y**2)

fx = lambda x: (x-1)**(1.0/3)

ans = euler(2, 1, -0.05, fxy, 1)

print('x        fx_true  fx_euler error')

for xy in ans:
    try:
        x = xy[0]
        x = 1 if x<1 else x
        fx_euler = xy[1]
        fx_gt = fx(x)
        #print('y(%f) = %f' % (xy[0], xy[1]))
        #print('error: %f' % (fx_euler - fx_gt))
        print('%.6f %.6f %.6f %.6f' % (x, fx_gt, fx_euler, fx_gt - fx_euler))    

    except Exception:
        print(x)
    


    