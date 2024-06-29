# list = ["hello", "world", "this", "is", "a", "test"]
# Output = ["hello","world"]  
# list.sort
# print(list[:2])


# list = [3,5,2,6,1,12,9]
# sum = 15
# print(list[0])

# input = "aabbcccdddd"
# output = "a2b3c3d4"

from collections import Counter
x = "aabbcccdddd"
y = Counter(x)
for keys,values in y.items():
    print(keys,values, end="")
    # print(f'{keys}{values}',end= '')

    