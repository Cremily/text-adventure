total_length = 0
class Node():
   def __init__(self):
       # Note that using dictionary for children (as in this implementation) would not allow lexicographic sorting mentioned in the next section (Sorting),
       # because ordinary dictionary would not preserve the order of the keys
       self.children = {}  # mapping from character ==> Node
       self.value = None

def find(node, key):
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value
def insert(root, string, value):
    global total_length
    node = root
    index_last_char = None
    for index_char, char in enumerate(string):
        if char in node.children:
            node = node.children[char]
        else:
            index_last_char = index_char
            break

    # append new nodes for the remaining characters, if any
    if index_last_char is not None: 
        for char in string[index_last_char:]:
            total_length += 1
            node.children[char] = Node()
            node = node.children[char]

    # store value in the terminal node
    node.value = value
base_node = Node()
numbers = ['0412578440', '0412199803', '0468892011', '112', '15']
for index,number in enumerate(numbers):
    insert(base_node,number,index)
print(total_length)