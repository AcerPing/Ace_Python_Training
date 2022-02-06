def reverse_vowle (string):
    vowel_string_list = []
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for each_letter in string:
        if each_letter.lower() in vowel_list:
            vowel_string_list.append(each_letter)
    vowel_string_list.reverse()
    print(vowel_string_list)
    return vowel_string_list

string = {}
vowel_string_list = reverse_vowle(string)
vowel_list = ['a', 'e', 'i', 'o', 'u']
reverse_list = []
for each_letter in string:
    if each_letter.lower() in vowel_list:
        reverse_list.append(vowel_string_list[0])
        del vowel_string_list[0]
    else:  reverse_list.append(each_letter)
print(reverse_list)
reverse_string = ''.join(reverse_list)
print(reverse_string)




'''
def reverse_vowle (string):
    vowel_string_list = []
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for each_letter in string:
        if each_letter in vowel_list:
            vowel_string_list.append(each_letter)
    vowel_string_list.reverse()
    print(vowel_string_list)
    return vowel_string_list

string = 'apple'
vowel_string_list = reverse_vowle(string)
vowel_list = ['a', 'e', 'i', 'o', 'u']
reverse_list = []
for each_letter in string:
    if each_letter in vowel_list:
        reverse_list.append(vowel_string_list[0])
        del vowel_string_list[0]
    else:  reverse_list.append(each_letter)
print(reverse_list)
reverse_string = ''.join(reverse_list)
print(reverse_string)
'''


# list_append = ['a', 'e', 'i', 'o', 'u']
# reverser_list = list_append.reverse()
# print(reverser_list)

# prime_numbers = [2, 3, 5, 7]
# prime_numbers.reverse()
# print('Reversed List:', prime_numbers)

# prime_numbers = ['a', 'e', 'i', 'o', 'u']
# prime_numbers.reverse()
# print('Reversed List:', prime_numbers)


