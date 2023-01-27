class Parentheses:
    def _init_(self, string):
        self.string = string
        self.stack = []

    def is_valid(self):
        for char in self.string:
            if char in "({[":
                self.stack.append(char)
            elif char in ")}]":
                if not self.stack:
                    return False
                if char == ")" and self.stack[-1] != "(":
                    return False
                if char == "{" and self.stack[-1] != "{":
                    return False
                if char == "[" and self.stack[-1] != "[":
                    return False
                self.stack.pop()
        if not self.stack:
            return True
        else:
            return False

string = input("enter a string of parentheses:")
p = Parentheses(string)
print(p.is_valid())