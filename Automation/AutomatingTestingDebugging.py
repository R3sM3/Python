#  Este codigo fue extraido desde la siguiente pagina
#  https://medium.com/@naseer1015922/5-killer-python-scripts-for-automation-part-2-33d7aa84cedc
#  Fue creado por https://medium.com/@naseer1015922

def longest_palindrome(s):
    n = len(s)
    ans = ""
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if substring == substring[::-1] and len(substring) > len(ans):
                ans = substring
    return ans

class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        self.assertEqual(longest_palindrome("a"), "a")
        self.assertEqual(longest_palindrome(""), "")

if __name__ == '__main__':
    unittest.main()
