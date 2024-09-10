# Write a function that reverses characters in (possibly nested) parentheses in the input string.

# Input strings will always be well-formed with matching ()s.

# Example

# For inputString = "(bar)", the output should be
# solution(inputString) = "rab";
# For inputString = "foo(bar)baz", the output should be
# solution(inputString) = "foorabbaz";
# For inputString = "foo(bar)baz(blim)", the output should be
# solution(inputString) = "foorabbazmilb";
# For inputString = "foo(bar(baz))blim", the output should be
# solution(inputString) = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".


def solution(inputString):
    def reverseString(nestedString):
        reversedString = ''
        for char in nestedString:
            reversedString = char + reversedString
        return reversedString

    hasNestedParentheses = True

    while hasNestedParentheses:
        parStart = 0
        parEnd = 0
        hasNestedParentheses = False

        for i in range(len(inputString)):
            if inputString[i] == '(':
                parStart = i
            elif inputString[i] == ')':
                parEnd = i
                nestedString = inputString[parStart + 1:parEnd]  # Extract the string inside parentheses
                reversedNestedString = reverseString(nestedString)
                inputString = inputString[:parStart] + reversedNestedString + inputString[parEnd + 1:]
                hasNestedParentheses = True  # Set the flag to True to indicate nested parentheses were found
                break  # Break the loop after processing one pair of parentheses

    return inputString