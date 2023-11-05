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
        self._stack.append(element)
    def pop(self):
        if len(self._stack) != 0:
            return self._stack.pop(-1)
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
        self._queue.append(element)
    def pop(self):
        if len(self._queue) != 0:
            return self._queue.pop(0)
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
class Matrix:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self._matrix = [[0 for j in range(M)] for i in range(N)]
    def get(self, line, col):
        if line > 0 and line < self._n and col > 0 and col < self._m:
            return None
        return self._matrix[line][col]
    def set(self, line, col, value):
        if line > 0 and line < self._n and col > 0 and col < self._m:
            return "Pozitii incorecte!"
        self._matrix[line][col] = value
    def transpose(self):
        transpose_matrix = Matrix(self._m, self._n)
        for line in range(self._n):
            for col in range(self._m):
                transpose_matrix[col][line] = self._matrix[line][col]
        return transpose_matrix



if __name__ == "__main__":
    # stack1 = Stack()
    # stack1.push([2, 3, 4, 5])
    # stack1.push("113")
    # stack1.push(("elem1", "elem2"))
    # stack1.push({1: 23, 2: 45})
    # print(stack1.pop(), stack1.pop(), stack1.pop(), stack1.pop())
    copy = copy_element({1: [1, 2, 3], 2: ("string1", "stingggg"), "salut": {1: 2, 3: 4}})
    print(copy)



