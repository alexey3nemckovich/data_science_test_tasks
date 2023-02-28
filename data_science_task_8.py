import random


def calc_central_tendency_measures(values):
    values_sum = 0
    values_frequency = {}
    max_frequency = 0

    for v in values:
        values_sum += v

        if v in values_frequency:
            values_frequency[v] += 1
        else:
            values_frequency[v] = 1

        if values_frequency[v] > max_frequency:
            max_frequency = values_frequency[v]

    average = values_sum / len(values)
    moda_values = [k for k, v in values_frequency.items() if v == max_frequency]

    moda_values_sum = 0
    for m in moda_values:
        moda_values_sum += m

    moda = moda_values_sum / len(moda_values)

    values.sort()
    median = values[len(values) // 2]
    if len(values) % 2 == 0 and len(values) > 1:
        median = (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2

    print(f"average = {average}")
    print(f"moda = {moda}")
    print(f"median = {median}")

    if average == moda == median:
        print("symmetric distribution")
    else:
        print("asymmetric distribution")


values_sample = []
rand = random.Random()
for i in range(100):
    values_sample.append(rand.randint(0, 100))
#values_sample = [1, 2, 2, 2, 5, 5, 5, 6]

print(values_sample)
calc_central_tendency_measures(values_sample)
