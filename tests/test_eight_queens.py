import unittest
from src.eight_queens import solve_n_queens

class TestEightQueens(unittest.TestCase):
    def test_n_4(self):
        """
        测试N=4的情况
        """
        solutions = solve_n_queens(4)
        # N=4应该有2个解决方案
        self.assertEqual(len(solutions), 2)
        
        # 验证每个解决方案是否有效
        for solution in solutions:
            self._validate_solution(solution, 4)
    
    def test_n_8(self):
        """
        测试N=8的情况
        """
        solutions = solve_n_queens(8)
        # N=8应该有92个解决方案
        self.assertEqual(len(solutions), 92)
        
        # 验证前几个解决方案是否有效
        for solution in solutions[:5]:
            self._validate_solution(solution, 8)
    
    def _validate_solution(self, solution, n):
        """
        验证解决方案是否有效
        """
        # 检查长度是否正确
        self.assertEqual(len(solution), n)
        
        # 检查是否有重复的列
        self.assertEqual(len(set(solution)), n)
        
        # 检查是否有对角线冲突
        for i in range(n):
            for j in range(i + 1, n):
                # 检查对角线冲突
                self.assertNotEqual(abs(solution[i] - solution[j]), abs(i - j))

if __name__ == '__main__':
    unittest.main()