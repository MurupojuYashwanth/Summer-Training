'''
di = {
    5:[7,3],
    7:[3,4,5],
    3:[5,7,8,13],
    4:[7,8,2],
    8:[3,4,2,10],
    2:[4,8,9],
    9:[2],
    10:[8,12],
    12:[10],
    13:[3]
}
'''
from collections import defaultdict
'''
di = {
    5:[(7,2,float('inf')),(3,5,float('inf'))],
    7:[(3,4,float('inf')),(4,6,float('inf')),(5,2,float('inf'))],
    3:[(5,5,float('inf')),(7,4,float('inf')),(8,2,float('inf'))],
    4:[(7,6,float('inf')),(8,4,float('inf')),(2,2,float('inf'))],
    8:[(3,2,float('inf')),(4,4,float('inf')),(2,5,float('inf'))],
    2:[(4,2,float('inf')),(8,5,float('inf'))]
}'''

di = {
    5:[(3,6,float('inf')),(7,1,float('inf'))],
    7:[(3,4,float('inf')),(4,4,float('inf')),(5,1,float('inf'))],
    3:[(5,6,float('inf')),(7,4,float('inf')),(8,11,float('inf'))],
    4:[(7,4,float('inf')),(8,5,float('inf')),(2,8,float('inf'))],
    8:[(3,11,float('inf')),(4,5,float('inf')),(2,5,float('inf'))],
    2:[(4,8,float('inf')),(8,5,float('inf'))]
}
# def bfstraversal(start,queue,visited,di):
#     queue.append(start)
#     while len(queue)>0:
#         for i in di[queue[0]]:
#             if (i not in visited) and (i not in queue):
#                 queue.append(i)
#         visited.append( queue.pop(0))
#     print(visited)
def dijikstrastraversal(start,di):
    queue = []
    visited = []
    d = defaultdict(lambda : float('inf'))
    d[start] = 0
    queue.append(start)
    while len(queue)>0:
        for i in di[start]:
            if (i[0] not in visited):
                queue.append(i[0])
                if d[start] + i[1] < d[i[0]]:
                    d[i[0]] = d[start] + i[1]
        if start not in visited:
            visited.append(start)
        queue.remove(start)
        if len(queue)>0:
            min = float('inf')
            for i in queue:
                if d[i] < min:
                    min = d[i]
                    start = i
    print()
    for i in visited:
        print(i,d[i])
#bfstraversal(5,[],[],di)
dijikstrastraversal(5,di)