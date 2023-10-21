"""
Stack = FIFO(FIRST IN FIRST OUT) data structure
        Stores objects into a sort of "Vertical tower"
        append() to add to the last(tail)
        pop(0) to remove from the First(head)
"""
# queue = []
# queue.append("First Item")
# queue.append("Second Item")
# queue.append("Third Item")
# queue.append("Fourth Item")

# print(queue)
# for x in range (4):
#     print(queue.pop(0))

from collections import deque
queue = deque()
for x in range(5):
    queue.append(f"Item {x+1}")

print(queue)
queue.popleft()
print(queue[0])