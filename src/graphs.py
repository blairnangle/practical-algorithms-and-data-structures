from collections import defaultdict
from itertools import product
import os
from collections import deque


def build_graph(words):

    # create a bucket with an empty list as the default values
    buckets = defaultdict(list)
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):

            # using .format to replace the letter at "i" with "_" - this is the name of a bucket
            bucket = '{}_{}'.format(word[:i], word[i + 1:])

            # either look up this bucket using its name (key in the dict) or create it
            # append `word` to the value list in the bucket
            # all these words in this bucket differ by exactly one letter (in the same place)
            # i.e., they all match the string pattern containing "_" above
            buckets[bucket].append(word)

    # print(buckets)

    # add vertices and edges for words in the same bucket
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def get_words(dict_file):
    for line in open(dict_file, 'r'):
        yield line[:-1]  # remove newline character


def traverse(graph, starting_vertex):
    visited = set()
    queue = deque([[starting_vertex]])
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])


if __name__ == "__main__":
    scrabble = os.path.join(os.path.dirname(__file__), 'scrabble.txt')
    word_graph = build_graph(get_words(scrabble))
    # for vertex, path in traverse(word_graph, 'FOOL'):
    #     if vertex == 'SAGE':
    #         print(' -> '.join(path))
    #         # FOOL -> FOOD -> FOLD -> SOLD -> SOLE -> SALE -> SAGE

    print(word_graph['FOOL'])
# set(['POOL', 'WOOL', 'FOWL', 'FOAL', 'FOUL', ... ])
