class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        
        rep = [[False]*n for row in matrix]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        cur_d = 0
        x_cur,y_cur = 0,0
        for i in range(m*n):
            spiral.append(matrix[y_cur][x_cur])
            rep[y_cur][x_cur] = True
            y_next = y_cur+dirs[cur_d][0]
            x_next = x_cur+dirs[cur_d][1]
            #print(y_cur,x_cur,cur_d,y_next,x_next,0 <= x_next < n,0 <= y_next <m)
            if (0 <= x_next < n) and (0 <= y_next < m) and (not rep[y_next][x_next]):
                y_cur = y_next
                x_cur = x_next
            else:
                cur_d += 1
                if cur_d > 3:
                    cur_d =0
                y_cur = y_cur+dirs[cur_d][0]
                x_cur = x_cur+dirs[cur_d][1]
            print(rep)
        return spiral