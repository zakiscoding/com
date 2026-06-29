from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q= deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minutes =0
        while q and fresh>0:
            for m in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nc = dc +c
                    nr=dr +r
                    if nc<0 or nr<0 or nc>=cols or nr>=rows:
                        continue
                    if grid[nr][nc]!=1:
                        continue
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            minutes+=1
        if fresh==0:
            return minutes
        return -1
                    
