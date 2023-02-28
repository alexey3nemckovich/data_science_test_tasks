import math


def calc_dice_probability(n, m, s):
    dice_max_value = 6

    if s > dice_max_value:
        print(f"Value can't be bigger then {dice_max_value}!")
        return

    if m > n:
        print(f"'m' can't be bigger then 'n'!")
        return

    p = 1
    if s > 0:
        p = ((dice_max_value - s) + 1) / dice_max_value

    q = 1 - p

    probability = 1
    if q != 0:
        m_n_combinations_count = math.factorial(n) / (math.factorial(n - m) * math.factorial(m))
        print(m_n_combinations_count)
        probability = m_n_combinations_count * p ** m * q ** (n - m)

    print(f"Probability that {m} times from {n} attempts dice will show value {s} or bigger equals {probability}")


calc_dice_probability(5, 4, 5)
