# str1 = "()"
# str2 = "[{()}]"
# str3 = "(){}[]"
# str4 = ""
# str5 = ")({}]["
# str6= "(]])"
# str7 = ")({}][[["
# str = '""{}()[]'
# Ouput = balanced/unbalanced

# def is_valid(s):
#     list = []
#     bracket = {')': '(', '}': '{', ']': '['}
    
#     for char in s:
#         if char in bracket:
#             top_element = list.pop() if list else '#'
#             if bracket[char] != top_element:
#                 return False
#         else:
#             list.append(char)
    
#     return not list









# Example usage:
# str1 = "()"
# str2 = "[{()}]"
# str3 = "(){}[]"
# str4 = ""
# str5 = ")({}]["
# str6 = "(]])"
# str7 = ")({}][[["

# Test cases
# print(is_valid(str1))  # True
# print(is_valid(str2))  # True
# print(is_valid(str3))  # True
# print(is_valid(str4))  # True (empty string)
# print(is_valid(str5))  # False
# print(is_valid(str6))  # False
# print(is_valid(str7))  # False

# my_array = [7, 12, 9, 4, 11]
# minVal = my_array[0]

# for i in my_array:
#     if i < minVal:
#         minVal = i

# print('Lowest value:',minVal)

#Python

# my_array = [7, 12, 3, 9,11,5,6,1]
# minval = my_array[0]
# print(minval)
# for i in my_array:
#     if i < minval:
#         minval = i
# print(minval)