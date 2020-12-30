from differentiate import d_scalar

def GD_steepest(f, x0, step, tol):
    """
    # steepest gradient descent
    #
    # example:
    # x, fx, search = GD_steepest(lambda x: x*x, 10, 0.1, 1e-33)
    """
    x = x0
    fx = f(x0)
    t = 1e10
    
    search = [(x, fx)]
    
    while t > tol:
        x_current = x
        f_current = f(x)
        g = d_scalar(f, x_current, 1e-10)
        x = x_current - step*g
        fx = f(x)
        
        t = abs(fx-f_current)
        search.append((x, fx))
    
    print(f"Min of f: ({x},{fx})")
    return x, fx, search
