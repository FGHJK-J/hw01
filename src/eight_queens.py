import time
import sys

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

def print_all_solutions(solutions):
    """
    打印所有解决方案
    """
    print(f"找到 {len(solutions)} 个解决方案：")
    for i, solution in enumerate(solutions, 1):
        print(f"解决方案 {i}：")
        print_solution(solution)

def visualize_solution(solution):
    """
    可视化解决方案
    """
    n = len(solution)
    # 打印棋盘顶部边框
    print('┌' + '─' * (2 * n - 1) + '┐')
    for row in solution:
        line = '│'
        for col in range(n):
            if col == row:
                line += 'Q'
            else:
                line += ' '
            if col < n - 1:
                line += ' '
        line += '│'
        print(line)
    # 打印棋盘底部边框
    print('└' + '─' * (2 * n - 1) + '┘')
    print()

def main():
    """
    主函数
    """
    # 解析命令行参数
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("错误：请输入有效的整数作为棋盘大小")
            return
    else:
        # 默认值
        n = 8
    
    # 检查输入值是否有效
    if n < 1:
        print("错误：棋盘大小必须大于0")
        return
    
    print(f"正在求解 {n} 皇后问题...")
    start_time = time.time()
    
    # 求解
    solutions = solve_n_queens(n)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 打印结果
    print(f"求解完成，共找到 {len(solutions)} 个解决方案")
    print(f"执行时间：{execution_time:.4f} 秒")
    
    # 如果解决方案数量较少，打印所有解决方案
    if len(solutions) <= 10:
        print_all_solutions(solutions)
    else:
        # 否则只打印前3个和后3个解决方案
        print("解决方案数量较多，只展示部分解决方案：")
        print("前3个解决方案：")
        for i, solution in enumerate(solutions[:3], 1):
            print(f"解决方案 {i}：")
            print_solution(solution)
        print("...")
        print("后3个解决方案：")
        for i, solution in enumerate(solutions[-3:], len(solutions) - 2):
            print(f"解决方案 {i}：")
            print_solution(solution)
    
    # 可视化第一个解决方案
    if solutions:
        print("第一个解决方案的可视化：")
        visualize_solution(solutions[0])

if __name__ == "__main__":
    main()