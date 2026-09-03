class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time, fresh = 0, 0
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = dr + r, dc + c
                    if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append([row, col])
            time += 1
        if fresh == 0:
            return time
        return -1
