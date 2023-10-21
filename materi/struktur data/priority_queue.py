""""
Queue that the first is the highest element and the last is the lowest one.
"""

from collections import deque

priority_queue = deque()

for x in range(12):
    priority_queue.append(x+1)

priority_queue.append(0)
list_convert = list(priority_queue)
list_convert.sort(reverse= True)

priority_queue = deque(list_convert)
for x in range(len(priority_queue)):
    print(priority_queue.popleft())

