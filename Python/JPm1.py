# def can_transform(a, b, c, d):
#     while a != c or b != d:
#         if a > c or b > d:
#             return "No"
#         a, b = a + b, b
#         # Check if b becomes zero, preventing an infinite loop
#         if b == 0:
#             return "No"
#     return "Yes"

# # Test cases
# result1 = can_transform(1, 4, 5, 9)
# result2 = can_transform(1, 4, 62, 45)

# print(result1)  # Should print "Yes"
# print(result2)  # Should print "Yes"


# #  this is wrong


def can_transform(a, b, c, d, count=0):
    print("Function run:", count)
    if a == c and b == d:
        return True
    if a > c or b > d:
        return False

    return can_transform(a + b, b, c, d, count + 1) or can_transform(a, a + b, c, d, count + 1)

# Test cases
result1 = can_transform(1, 4, 5, 9)
result2 = can_transform(1, 4, 62, 45)

print(result1)  # Should print "True"
print(result2)  # Should print "True"
