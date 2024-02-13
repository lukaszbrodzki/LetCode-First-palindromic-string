class Solution:
    def firstPalindrome(self, words: [str]) -> str:
        def is_palindrome(w: str) -> bool:
            for letter in range(len(w)):
                i = letter
                j = len(w) - i - 1

                if j < i:
                    return True
                if w[i] != w[j]:
                    return False
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""

    def firstPalindrome2(self, words: [str]) -> str:
        ''' Faster solution '''
        def is_palindrome(w: str) -> bool:
            length = len(w)
            for i in range(length):
                j = length - i - 1

                if j < i:
                    return True
                if w[i] != w[j]:
                    return False
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""

    def firstPalindrome3(self, words: [str]) -> str:
        ''' Faster solution '''
        def is_palindrome(w: str) -> bool:
            start = 0
            end = len(w) - 1

            while start < end:
                if w[start] != w[end]:
                    return False
                start += 1
                end -= 1

            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""

    def firstPalindrome4(self, words: [str]) -> str:
        ''' Faster solution '''
        for word in words:
            start = 0
            end = len(word) - 1

            while start < end:
                if word[start] != word[end]:
                    break
                start += 1
                end -= 1

            if start >= end:
                return word
        return ""


if __name__ == '__main__':
    solution = Solution()
    words = ["abc","car","ada","racecar","cool"]
    print(solution.firstPalindrome4(words))
