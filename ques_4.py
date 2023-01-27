import string

def is_pangaram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False

        return True

string = ' the quick brown fox jumps over the lazy dog'
if (is_pangaram(string) == True):
    print("yes")
else:
    print("no")