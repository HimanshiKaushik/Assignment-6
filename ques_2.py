def palindrome(string):
    return string == string[::-1]

s = input("enter a word : ")
print(palindrome(s))