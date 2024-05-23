class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # idea: can have stack which takes in only open brackets at all times, and then when it encounters a close bracket, it can pop the last item from the stack and check if the popped item is the corresponding open bracket

        # need to know the matching or same type open brackets
        matchingTypes = {')': '(', '}': '{', ']': '['}

        # initialize stack (last in, first out)
        stack = []
        open_brackets = ['(', '{', '[']
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if len(stack) == 0 or matchingTypes[i] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True

def test_isValid():
    solution = Solution()
    
    # test cases
    test_cases = [
        {"input": "()", "expected": True},
        {"input": "()[]{}", "expected": True},
        {"input": "(]", "expected": False},
        {"input": "([)]", "expected": False},
        {"input": "{[]}", "expected": True},
        {"input": "(", "expected": False},
        {"input": "]", "expected": False},
        {"input": "([{}])", "expected": True},
        {"input": "(([]){})", "expected": True},
        {"input": "(([]){}[", "expected": False},
    ]
    
    for case in test_cases:
        result = solution.isValid(case["input"])
        assert result == case["expected"], f"Failed: input({case['input']}) => output({result}), expected({case['expected']})"
        print(f"Passed: input({case['input']}) => output({result})")

# run the test cases
test_isValid()
