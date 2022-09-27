def palindrome(string, index):
    if index >= len(string) // 2:
        return f"{string} is a palindrome"
    if not string[index] == string[-1 - index]:
        return f"{string} is not a palindrome"
    return palindrome(string, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
