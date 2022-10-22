from collections import deque

size = 50
eggs = deque([int(s) for s in input().split(', ')])
papers = deque([int(s) for s in input().split(', ')])
count_boxes = 0
while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = papers.pop()
    if paper + egg <= size:
        count_boxes += 1
if count_boxes:
    print(f"Great! You filled {count_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if papers:
    print(f'Pieces of paper left: {", ".join(map(str, papers))}')
