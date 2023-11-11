def copy_element(element):
    if isinstance(element, dict):
        copy_dict = {}
        for key in element:
            copy_dict[key] = copy_element(element[key])
        return copy_dict

    elif isinstance(element, list):
        copy_list = []
        for item in element:
            copy_list.append(copy_element(item))
        return copy_list

    elif isinstance(element, set):
        copy_set = {}
        for item in element:
            copy_set.add(copy_element(item))
        return copy_set

    elif isinstance(element, tuple):
        copy_tuple = []
        for item in element:
            copy_tuple.append(copy_element(item))
        return tuple(copy_tuple)

    else:
        return element
class Stack:
    def __init__(self):
        self._stack = []
    def push(self, element):
        self._stack.append(copy_element(element))
    def pop(self):
        if len(self._stack) != 0:
            return copy_element(self._stack.pop(-1))
        return None

    def peek(self):
        if len(self._stack) != 0:
            element = copy_element(self._stack[-1])
            return element
        return None
    def clear(self):
        if len(self._stack):
            while len(self._stack):
                self._stack.remove(0)
        else:
            return "Already empty stack"
    def is_empty(self):
        if len(self._stack) == 0:
            return True
        return False

class Queue:
    def __init__(self):
        self._queue = []
    def push(self, element):
        self._queue.append(copy_element(element))
    def pop(self):
        if len(self._queue) != 0:
            return copy_element(self._queue.pop(0))
        return None
    def peek(self):
        if len(self._queue):
            element = copy_element(self._queue[0])
            return element
        return None
    def clear(self):
        if len(self._queue):
            while len(self._queue):
                self._queue.remove(0)
        else:
            return "Already empty stack"
    def is_empty(self):
        if len(self._queue) == 0:
            return True
        return False

#ex3
class Matrix:
    def __init__(self, N, M):
        if N < 0 or M < 0:
            return "Give positive parameters."
        self._n = N
        self._m = M
        self._matrix = [[0 for j in range(M)] for i in range(N)]
    def get(self, line, col):
        return self._matrix[line][col]
        return None
    def get_number_lines(self):
        return self._n
    def get_number_cols(self):
        return self._m
    def set(self, line, col, value):
        self._matrix[line][col] = value
    def transpose(self):
        transpose_matrix = Matrix(self._m, self._n)
        for line in range(self._n):
            for col in range(self._m):
                transpose_matrix.set(col, line, self._matrix[line][col])
        return transpose_matrix

    #Inmultirea matricilor care contin doar numere
    def multiply(self, other_matrix):
        if self._m != other_matrix.get_number_lines():
            return "Number of cols matrix1 !=  number of lines matrix2!"

        for i in range(self._n):
            for j in range(self._m):
                if not isinstance(self._matrix[i][j], (int, float)):
                    return "The elements of matrix 1 aren't numbers!"

        for i in range(other_matrix.get_number_lines()):
            for j in range(other_matrix.get_number_cols()):
                if not isinstance(other_matrix.get(i, j), (int, float)):
                    return "The elements of matrix 2 aren't numbers!"

        result_matrix = Matrix(self._n, other_matrix.get_number_cols())
        for i in range(self._n):
            for j in range(other_matrix.get_number_cols()):
                for k in range(self._m):
                    result_matrix.set(i, j, result_matrix.get(i, j) + self._matrix[i][k] * other_matrix.get(k, j))
        return result_matrix

    #Inmultirea matricii cu un numar
    def multiply_by_number(self, number):
        if not isinstance(number, (int, float)):
            return "The parameter isn't a number!"

        for i in range(self._n):
            for j in range(self._m):
                if not isinstance(self._matrix[i][j], (int, float)):
                    return "The elements of matrix aren't numbers!"
        result_matrix = Matrix(self._n, self._m)
        for i in range(self._n):
            for j in range(self._m):
                result_matrix.set(i, j, number * self._matrix[i][j])

        return result_matrix

    def apply_function(self, function):
        if not callable(function):
            return "Incorrect lambda function!"
        result_matrix = Matrix(self._n, self._m)
        for i in range(self._n):
            for j in range(self._m):
                result_matrix.set(i, j, function(self._matrix[i][j]))
        return result_matrix
    def type_element(self, line, col):
        if line >= 0 and line < self._n and col >= 0 and col < self._m:
            return type(self._matrix[line][col])
        return "Incorrect positions!"

    def get_string(self):
        matrix_str = ""
        for row in self._matrix:
            for item in row:
                matrix_str = matrix_str +  str(item) + " "
            matrix_str += "\n"
        return matrix_str



if __name__ == "__main__":
    stack1 = Stack()
    stack1.push([2, 3, 4, 5])
    stack1.push("113")
    stack1.push(("elem1", "elem2"))
    stack1.push({1: 23, 2: 45})
    print(stack1.pop(), stack1.pop(), stack1.pop(), stack1.peek())

    ######Test function copy
    # element = {1: [1, 2, 3], 2: ("string1", "stingggg"), "salut": {1: 2, 3: 4}}
    # copy = copy_element(element)
    # copy[1].remove(2)
    # copy["salut"] = ""
    # print(element)
    # print(copy)
    matrix1 = Matrix(2, 3)
    matrix1.set(0, 0, 1)
    matrix1.set(0, 1, 2)
    matrix1.set(0, 2, 3)
    matrix1.set(1, 0, 4)
    matrix1.set(1, 1, 5)
    matrix1.set(1, 2, 6)

    matrix2 = Matrix(3, 3)
    matrix2.set(0, 0, 7)
    matrix2.set(0, 1, 8)
    matrix2.set(0, 2, 2)
    matrix2.set(1, 0, 9)
    matrix2.set(1, 1, 10)
    matrix2.set(1, 2, 10)
    matrix2.set(2, 0, 11)
    matrix2.set(2, 1, 12)
    matrix2.set(2, 2, 0)

    matrix3 = matrix1.multiply(matrix2)
    print(matrix3.get_string())

    matrix4 = matrix3.transpose()
    print(matrix4.get_string())

    print(matrix4.apply_function(lambda x: x % 5).get_string())

    matrix5 = matrix3.apply_function(lambda x: str(x) + "string")
    print(matrix5.get_string())

    print(matrix5.type_element(0, 0))

    print(matrix5.multiply_by_number(2))

    print(matrix3.multiply_by_number(2).get_string())

    print(matrix3.get(-1, 0))




