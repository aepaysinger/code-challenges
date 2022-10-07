class Vector:
    def __init__(self, values):
        self.values = values
        self._length = 0
        for value in self.values:
            self._length += 1

    def __eq__(self, vector):
        return self.values == vector.values

    def equals(self, vector):
        return self.values == vector.values

    def __str__(self):
        vector_str = "("
        for value in self.values:
            vector_str += str(value) + ","
        vector_str = vector_str[:-1] + ")"

        return vector_str

    def add(self, vector):
        if self._length != vector._length:
            raise ValueError("Vectors must be the same length")
        else:
            return Vector([sum(x) for x in zip(self.values, vector.values)])

    def subtract(self, vector):
        if self._length != vector._length:
            raise ValueError("Vectors must be the same length")
        else:
            sub_vector = []
            for i, value in enumerate(self.values):
                sub_value = self.values[i] - vector.values[i]
                sub_vector.append(sub_value)

            return Vector(sub_vector)

    def dot(self, vector):
        if self._length != vector._length:
            raise ValueError("Vectors must be the same length")
        else:
            dot_vector = []
            for i, value in enumerate(self.values):
                dot_value = self.values[i] * vector.values[i]
                dot_vector.append(dot_value)

            return sum(dot_vector)

    def norm(self):
        norm_values = []
        for value in self.values:
            norm_values.append(pow(value, 2))

        return sum(norm_values)

    def tostring(self):
        return str(self)
