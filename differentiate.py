def d_scalar(f, x, eps):
    """
    example:
    d_scalar(lambda x: x*x, 2, 0.001)
    """
    return (f(x+eps)-f(x-eps))/(2*eps)