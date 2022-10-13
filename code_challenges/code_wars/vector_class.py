import math


class Vector:
    def __init__(self, values):
        self._values = values

    def __eq__(self, vector):
        return self._values == vector._values

    def equals(self, vector):
        return self == vector

    def __str__(self):
        vector_str = "("
        for value in self._values:
            vector_str += str(value) + ","
        vector_str = vector_str[:-1] + ")"

        return vector_str

    def add(self, vector):
        if len(self) != len(vector):
            raise ValueError("Vectors must be the same length")
        else:
            return Vector([sum(x) for x in zip(self._values, vector._values)])

    def subtract(self, vector):
        if len(self) != len(vector):
            raise ValueError("Vectors must be the same length")
        else:
            sub_vector = []
            for i, value in enumerate(self._values):
                sub_value = self._values[i] - vector._values[i]
                sub_vector.append(sub_value)

            return Vector(sub_vector)

    def dot(self, vector):
        if len(self) != len(vector):
            raise ValueError("Vectors must be the same length")
        else:
            dot_vector = []
            for i, value in enumerate(self._values):
                dot_value = self._values[i] * vector._values[i]
                dot_vector.append(dot_value)

            return sum(dot_vector)

    def norm(self):
        norm_values = []
        for value in self._values:
            norm_values.append(pow(value, 2))

        return math.sqrt(sum(norm_values))

    def tostring(self):
        return str(self)

    def __len__(self):
        return len(self._values)
