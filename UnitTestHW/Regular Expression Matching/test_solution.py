import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

# Test cases for regular expression matching
# Format: (s, p, expected_result)
testcases = [
    ("", "", True),
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("a", ".*.", True),
    ("aab", "c*a*b", True),
    ("aaa", "ab*a*c*a", True)
]

@pytest.mark.parametrize("s, p, expected_result", testcases)
def test_is_match(solution, s, p, expected_result):
    assert solution.isMatch(s, p) == expected_result

@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch("aaa", "aa")
