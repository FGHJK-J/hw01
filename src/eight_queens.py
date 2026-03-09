def solve_n_queens(n):
    """
    解决N皇后问题
    参数:
        n: 棋盘大小
    返回:
        所有可能的解决方案，每个解决方案是一个列表，
        其中每个元素表示对应行的皇后位置
    """
    solutions = []
    # 记录每一行的皇后位置
    board = [-1] * n
    
    def is_safe(row, col):
        """
        检查在(row, col)位置放置皇后是否安全
        """
        for i in range(row):
            # 检查列冲突
            if board[i] == col:
                return False
            # 检查对角线冲突
            if abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(row):
        """
        回溯算法解决N皇后问题
        """
        if row == n:
            # 找到一个解决方案
            solutions.append(board.copy())
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    
    backtrack(0)
    return solutions

def print_solution(solution):
    """
    打印解决方案
    """
    n = len(solution)
    for row in solution:
        line = ['.'] * n
        line[row] = 'Q'
        print(''.join(line))
    print()