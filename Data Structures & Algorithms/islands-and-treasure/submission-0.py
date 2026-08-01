from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        row=len(grid)
        col=len(grid[0])

        queue=deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    queue.append((i,j))
        
        print(queue)
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        level=1
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==2147483647:
                        grid[nr][nc]=level
                        queue.append((nr,nc))

            level+=1

        




        