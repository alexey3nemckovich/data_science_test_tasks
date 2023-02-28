def f_sample(x):
    return 3 * x ** 3 + 4 * x ** 2 ##+ 5 * x + 21


# Function f(x) = 3x^3 + 4x^2 + 5x + 21 increases value over the entire domain of definition:
# f'(x) = 9x^2 + 8x + 5 > 0 always.
# That's why in [a, b] range it always has minimum in x=a.
def f_specific_min_impl(a, b, e):
    return a


# Below are listed some more universal ways to find minimum of defined function
def get_x_min_in_range_dichotomy(a, b, e, f):
    while abs(b - a) > e:
        x = (a + b) / 2
        f1 = f(x - e)
        f2 = f(x + e)
        if f1 < f2:
            b = x
        else:
            a = x
    return (a + b) / 2


def get_x_min_in_range_golden_ration(a, b, e, f):
    t1 = 0.381966
    t2 = 1 - t1
    x1 = a + (b - a) * t1
    x2 = a + (b - a) * t2
    f1 = f(x1)
    f2 = f(x2)
    while abs(b - a) > e:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (b - a) * t1
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) * t2
            f2 = f(x2)
    return (a + b) / 2


print(get_x_min_in_range_dichotomy(-0.5, 5, 0.01, f_sample))
print(get_x_min_in_range_golden_ration(-0.5, 5, 0.01, f_sample))
