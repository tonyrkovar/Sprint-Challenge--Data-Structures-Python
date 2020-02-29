import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
"""
This problem as it is written is O(n^2). Because we're going to be iterating over two separate files and when we iterate over the first one, we're comparing every single element in the second file against a single element in the first.
Since you are comparing the second list to every single element in the first you're going to be iterating list1 * list2 incredibly inefficiently.
"""
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

name_tree = BinarySearchTree('Tony Kovar')
for name in names_1:
    name_tree.insert(name)

for name2 in names_2:
    if name_tree.contains(name2):
        print(name2)
        duplicates.append(name2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

## vvv Run time for original here as well
"""
This problem as it is written is O(n^2). Because we're going to be iterating over two separate files and when we iterate over the first one, we're comparing every single element in the second file against a single element in the first.
Since you are comparing the second list to every single element in the first you're going to be iterating list1 * list2 incredibly inefficiently.
"""

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
