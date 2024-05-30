import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = 1
            else:
                return True
        return False

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_no_duplicate(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4, 5]))

    def test_contains_duplicate(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_single_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))

    def test_large_input(self):
        self.assertTrue(self.solution.containsDuplicate(list(range(10000)) + [1]))

    def test_all_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 1, 1]))

    def test_no_duplicates_with_negative_numbers(self):
        self.assertFalse(self.solution.containsDuplicate([-1, -2, -3, -4]))

    def test_duplicates_with_negative_numbers(self):
        self.assertTrue(self.solution.containsDuplicate([-1, -2, -3, -1]))

if __name__ == '__main__':
    unittest.main()
