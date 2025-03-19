# def count_occurrences(lst, element):
#     count = 0
#     for item in lst:
#         if item == element:
#             count += 1
#     return count
#
# # Example usage
# sample_list = [2, 4, 1, 7, 9, 10, 12, 17, 1]
# element_to_count = 10
# result = count_occurrences(sample_list, element_to_count)
# print(f"{element_to_count} occurs {result} times in the list.")

def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1  # Increment count if item exists
        else:
            count_dict[item] = 1  # Initialize count if item does not exist
    return count_dict

# Example usage
sample_list = [2, 4, 1, 7, 9, 10, 12, 17, 1, 4, 2, 2]
result = count_occurrences(sample_list)
for i,j in result.items():
    print(f"Key {i} has occured {j} times")


text = "Hello, world! Welcome to the world of Python."
# Dictionary to store character counts
char_count_dict = {}
for char in text:
    if char in char_count_dict:
        char_count_dict[char] += 1
    else: char_count_dict[char] = 1

# Print the dictionary print