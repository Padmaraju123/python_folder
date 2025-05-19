"""
Input : test_str = 'geeks are for geeksforgeeks', que_word = "geek"
Output : {'s': 3}
"""
#
# sent_li = input("Enter the sentence : ").split(" ")
# word = input("Enter the word to search in given sentence: ")
#
#
# dk = {ww:ww.count(word) for ww in sent_li}
# print(dk)

s = input()

has_num = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for c in s:
    if not has_num and c.isalnum():
        has_num = True
    if not has_alpha and c.isalpha():
        has_alpha = True
    if not has_digit and c.isdigit():
        has_digit = True
    if not has_lower and c.islower():
        has_lower = True
    if not has_upper and c.isupper():
        has_upper = True

print(has_num)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)
