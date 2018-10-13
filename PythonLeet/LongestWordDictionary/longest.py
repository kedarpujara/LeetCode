# class Trie(object):
#     def __init__(self, char: str):
#         self.char = char
#         self.children = []
#         self.word_finished = False
#         self.counter = 1

# def add(root, word: str):
#     node = root
#     for char in word:
#         found_in_child = False
        
array = [1,2,3,4,5,6,7,8,9]
length = len(array)
mid = length//2

first = array[:mid]
second = array[mid+1:]
print(array[mid])
print(first)
print(second)