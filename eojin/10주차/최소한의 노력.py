from typing import List
import heapq
import math

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def minimumEffortPath(heights: List[List[int]]) -> int:
    row,col = map(len, (heights, heights[0]))
    efforts = [[math.inf] * col for _ in range(row)]
    efforts[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        effort, x, y = heapq.heappop(heap)
        if (x, y) == (row - 1, col - 1):
            return effort
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<row and ny>=0 and ny<col:
                next_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                if efforts[nx][ny] > next_effort:
                    efforts[nx][ny] = next_effort
                    heapq.heappush(heap, (next_effort, nx, ny))


print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))