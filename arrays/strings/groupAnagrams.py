class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {}

        for word in strs:
            letters = ''.join(sorted(word))
            if letters in anagrams:
                anagrams[letters].append(word)
            else:
                anagrams[letters] = [word]

        grpAnagrams = []
        for key in anagrams:
            grpAnagrams.append(anagrams[key])
        return grpAnagrams

def test_groupAnagrams():
    solution = Solution()
    
    # Test cases
    test_cases = [
        {"input": ["eat", "tea", "tan", "ate", "nat", "bat"], "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]},
        {"input": [""], "expected": [[""]]},
        {"input": ["a"], "expected": [["a"]]},
    ]
    
    for case in test_cases:
        result = solution.groupAnagrams(case["input"])
        # Sort inner lists and the outer list to ensure the comparison is order-agnostic
        result = [sorted(group) for group in sorted(result, key=lambda x: (len(x), x))]
        expected = [sorted(group) for group in sorted(case["expected"], key=lambda x: (len(x), x))]
        assert result == expected, f"Failed: input({case['input']}) => output({result}), expected({expected})"
        print(f"Passed: input({case['input']}) => output({result})")

test_groupAnagrams()
