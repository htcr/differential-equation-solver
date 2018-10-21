import numpy as np

def rk4(start, end, h, f, y_start):
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
        
        k1 = h*f(cur_x, cur_y)
        k2 = h*f(cur_x+h/2.0, cur_y+k1/2.0)
        k3 = h*f(cur_x+h/2.0, cur_y+k2/2.0)
        k4 = h*f(cur_x+h, cur_y+k3)

        cur_y += (1.0/6)*(k1+2*k2+2*k3+k4)
        cur_x += h

    ans.append((cur_x, cur_y))
    
    return ans    

fxy = lambda x, y: 1.0 / (3*(y**2))

#fxy = lambda x, y: -(y**2)

fx = lambda x: (x-1)**(1.0/3)

#fx = lambda x: 1.0 / x

ans = rk4(2, 1, -0.05, fxy, 1)

#ans = rk4(1, 2, 0.1, fxy, 1)

print('x        fx_true  fx_rk4   error')

for xy in ans:
    try:
        x = xy[0]
        x = 1 if x<1 else x
        fx_approx = xy[1]
        fx_gt = fx(x)
        #print('y(%f) = %f' % (xy[0], xy[1]))
        #print('error: %f' % (fx_euler - fx_gt))
        print('%.6f %.6f %.6f %.6f' % (x, fx_gt, fx_approx, fx_gt - fx_approx))    

    except Exception:
        print(x)
    


    