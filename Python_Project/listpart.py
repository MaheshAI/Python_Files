# list_items = ["hello", "world", "this", "is", "a", "test"]
# sorted_list = sorted(list_items, key=len, reverse=True)
# output = sorted_list[:2]
# print(output)

# list_items = ["hello", "world", "this", "is", "a", "test"]
# sorted_list = sorted(list_items,key=len, reverse=True)
# print(sorted_list[:2])


# Initial list with mixed types
lst = ["hello", 1, 2, 3, 3, 4, 5, 6]

# Lists to keep track of seen and duplicate numbers
seen = []
duplicates = []

# Loop through the list and check for duplicates
for item in lst:
       if item in seen:
            duplicates.append(item)
       else:
            seen.append(item)

# Print the duplicates
print("Duplicate numbers:", duplicates)
print("numbers:", seen)


                

