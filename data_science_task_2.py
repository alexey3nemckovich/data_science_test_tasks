import math


def is_zero_vector(vector: list[float]):
    return all(v == 0 for v in vector)


def calc_vector_scalar_prod(vector_1, vector_2):
    return sum([x * y for x, y in zip(vector_1, vector_2)])


def calc_vector_norm(vector):
    return math.sqrt(calc_vector_scalar_prod(vector, vector))


def calc_vectors_similarity(vector_1, vector_2):
    if is_zero_vector(vector_1) or is_zero_vector(vector_2):
        print("Failed to calculate vectors similarity: zero vectors are not allowed!")
        return

    scalar_prod = calc_vector_scalar_prod(vector_1, vector_2)
    vector_1_norm = calc_vector_norm(vector_1)
    vector_2_norm = calc_vector_norm(vector_2)

    print(scalar_prod / (vector_1_norm * vector_2_norm))


vector_1_sample = [1, 2, 3]
vector_2_sample = [3, 4, 12321]
calc_vectors_similarity(vector_1_sample, vector_2_sample)
