from typing import List

'''
Furdui Dimitrie-Toma
https://en.wikipedia.org/wiki/Greedy_coloring
'''
class Edge:
    def __init__(self, source: int, destination: int):
        self._source = source
        self._destination = destination

    @property
    def source(self):
        return self._source

    @property
    def destination(self):
        return self._destination


class Graph:
    _adjacency_list: List[List[int]]
    _size: int

    def __init__(self, edges: List[Edge], size: int):
        self._adjacency_list = [[] for _ in range(size)]
        self._size = size
        for edge in edges:
            self._adjacency_list[edge.source].append(edge.destination)
            self._adjacency_list[edge.destination].append(edge.source)

    def color(self):
        colors = {}
        for vertex in range(self._size):
            adjacent_colors = set([
                colors[adjacent]
                for adjacent in self._adjacency_list[vertex]
                if adjacent in colors
            ])
            color = next(i for i in range(self._size) if i not in adjacent_colors)
            colors[vertex] = color
        return colors


if __name__ == "__main__":
    size = 8
    edges = [
        Edge(a, b)
        for a, b in [
            (0, 4),
            (0, 6),
            (0, 2),
            (4, 7),
            (7, 3),
            (6, 1),
            (4, 5),
            (5, 1)
        ]
    ]
    graph = Graph(edges, size)
    colors = graph.color()
    for i in range(size):
        print(f"vertex {i} has the color {colors[i]}")
    print(f"--> with a total of {max(colors.values()) + 1} colors")



"""
-= Edit distance =-

Given two strings str1 and str2, the operations below that can performed on str1. Find minimum number of operations to
convert ‘str1’ into ‘str2’.

Operations:
    1. Insert character
    2. Remove character
    3. Replace character
All of the above operations are of equal cost.

where?

"""

# str1 = 'Harry'
# str2 = 'Blackberry'


str1 = 'abracadabra'
str2 = 'alohomora 1234'

# str1 -> str2
# Harry -> Blackberry => Ha -> Blackbe (cost 0) => Bla -> Blackbe (cost 2) =>  -> ckbe (cost 2) => ckbe->ckbe (cost 2+4)
# total cost is 6

'''
V1 -> Brute force 
'''


# str1 -> str2
def edit_distance_bf(str1, str2):
    # transform empty string into non-empty one
    if len(str1) == 0:
        return len(str2)
    # transform a string into an empty one
    if len(str2) == 0:
        return len(str1)

    # last character is common to both strings
    if str1[-1] == str2[-1]:
        return edit_distance_bf(str1[:-1], str2[:-1])

    # we need to do an operation. which one is best !?
    # minimum cost of inserting, remove or replacing a character in str1, respectively
    return 1 + min(edit_distance_bf(str1, str2[:-1]), edit_distance_bf(str1[:-1], str2),
                   edit_distance_bf(str1[:-1], str2[:-1]))


# print(edit_distance_bf(str1, str2))

'''
V2 -> Dynamic programming

!! Dynamic programming is (in most cases) just a way to optimize recursion 
'''
from texttable import Texttable


def pretty_print(T, str1, str2):
    t = Texttable()
    t.header('  ' + str1)

    for i in range(len(T)):
        t.add_row([str2[i - 1] if i > 0 else ' '] + T[i])

    print(t.draw())


# str1 -> str2
def edit_distance_dp(str1, str2):
    n = len(str1)
    m = len(str2)

    # Build a table of (interim) values
    T = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Fill in table for basic case (one of the strings is empty)
    for i in range(n + 1):
        T[0][i] = i
    for j in range(m + 1):
        T[j][0] = j

    # Fill in table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Case where last character is common to str1, str2
            if str1[i - 1] == str2[j - 1]:
                T[j][i] = T[j - 1][i - 1]
            else:
                T[j][i] = 1 + min(T[j - 1][i], T[j][i - 1], T[j - 1][i - 1])
    pretty_print(T, str1, str2)


edit_distance_dp(str1, str2)

"""
Grebla Mihai (913)

A labyrinth is given as a matrix of n rows and m columns, where 0 represents an empty space and 1 is a blocked space
You start from the top-left corner and you need to get to the bottom right corner. You are allowed to move
only in 4 directions N-E-S-W. Compute the length of the shortest path from start to finish.
"""
from collections import deque


def get_matrix():
    try:
        f = open("input.txt", "r")
        line = f.readline()
        tokens = line.strip().split(' ')
        n = int(tokens[0])
        m = int(tokens[1])
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            line = f.readline()
            tokens = line.strip().split(' ')
            for j in range(m):
                matrix[i][j] = int(tokens[j])
        f.close()
        return n, m, matrix
    except IOError as e:
        raise e


def print_matrix(labyrinth):
    for i in range(len(labyrinth)):
        print(labyrinth[i])

    print("<====================>")


def search(n, m, q, mat):
    dl = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    viz = [[0 for j in range(m)] for i in range(n)]
    viz[0][0] = 1
    while q:
        top = q.popleft()
        lin = top[0]
        col = top[1]
        for i in range(4):
            new_lin = lin + dl[i]
            new_col = col + dc[i]
            if m > new_col >= 0 and n > new_lin >= 0:
                if viz[new_lin][new_col] == 0 and 0 == mat[new_lin][new_col]:
                    viz[new_lin][new_col] = viz[lin][col] + 1
                    q.append((new_lin, new_col))
    print_matrix(viz)
    return viz[n - 1][m - 1] - 1


def main():
    data = get_matrix()
    n = data[0]
    m = data[1]
    labyrinth = data[2]
    print_matrix(labyrinth)
    q = deque()
    q.append((0, 0))
    result = search(n, m, q, labyrinth)
    print("The minimum number of steps is:", result)


main()
