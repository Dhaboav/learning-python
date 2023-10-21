from collections import deque
"""
Stack = LIFO(Last In First Out) data structure
        Stores objects into a sort of "Vertical tower"
        append() to add to the top
        pop() to remove from the top
"""

# # Using list
# stack = []
# # Use append method to replace push method in java!
# # append method add item to the last indeks
# print("Push value to stack:\n")
# stack.append("Item 1")
# stack.append("Item 2")
# stack.append("Item 3")
# stack.append("Item 4")
# print(f"Result: {stack}")
# print(f"The top stacked: {stack[-1]}")

# # Check item ada atau tidak
# if "Item 1" in stack:
#     print("true")
# else:
#     print("false")

# # to access the first item: use pop method
# print("POP Method: ")
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(f"Result: {stack}")

# for x in range(100):
#     stack.append(f"Item {x}")

# print(stack)


# using deque
stack = deque()
for x in range(10):
    stack.append(f"Item {x+1}")

print(stack)
for y in range (5):
    stack.pop()

print(stack[-1])