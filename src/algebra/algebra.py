from numpy.linalg import norm


class Algebra:

    @staticmethod
    def sum(vector_a, vector_b):
        return vector_a + vector_b

    @staticmethod
    def dist(vector_a, vector_b):
        return norm(vector_a - vector_b, ord=1)

    @staticmethod
    def mult(vector_a, vector_b=None, k=1):
        if vector_b is not None:
            return vector_a * vector_b
        return vector_a * k
